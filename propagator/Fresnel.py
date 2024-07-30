import numpy as np
    
class Fresnel:
    @staticmethod
    def propagate(source, source_resolution, lam, z):
        # Propagator configuration
        M, N = source.shape[0], source.shape[1]    
        if M!=N:
            raise ValueError("Input image must have the same height and width")
        
        x0 = source_resolution * np.arange(-N/2, N/2)
        y0 = source_resolution * np.arange(-N/2, N/2)
        X0, Y0 = np.meshgrid(x0, y0)
        # prevent spherical wave aliasing
        spherical_wave_aliasing_limit = z/np.sqrt((2*source_resolution/lam)**2 - 1)
        phase_0 = np.exp(1j*np.pi/lam/z * (X0**2 + Y0**2))
        phase_0[np.abs(X0)>=spherical_wave_aliasing_limit] = 0
        phase_0[np.abs(Y0)>=spherical_wave_aliasing_limit] = 0

        fresnel = source * phase_0
        fresnel = np.fft.fftshift(np.fft.fft2(fresnel))

        # on a hologram plane
        dx = lam*z/N/source_resolution
        x = dx * np.arange(-N/2, N/2)
        y = dx * np.arange(-N/2, N/2)
        X, Y = np.meshgrid(x, y)

        # prevent spherical wave aliasing
        phase_1 = (1/1j/lam/z) * np.exp(1j*2*np.pi/lam * z) * np.exp(1j*np.pi/lam/z * (X**2 + Y**2))
        spherical_wave_aliasing_limit = z/np.sqrt((2*dx/lam)**2 - 1)
        phase_1[np.abs(X)>=spherical_wave_aliasing_limit] = 0
        phase_1[np.abs(Y)>=spherical_wave_aliasing_limit] = 0

        fresnel = fresnel * phase_1
        
        return fresnel, dx
