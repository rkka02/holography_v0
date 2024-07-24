import numpy as np

class Fresnel_propagator:
    @staticmethod
    def propagate(lam, z, source, source_resolution):
        # Propagator configuration
        M, N = source.shape[0], source.shape[1]    
        if M!=N:
            raise ValueError("Input image must have the same height and width")
        
        # before fourier transform
        x0m = source_resolution * np.arange(-N//2, N//2)
        y0n = source_resolution * np.arange(-N//2, N//2)
        X0m, Y0n = np.meshgrid(x0m, y0n)
        
        phase_0 = np.exp(1j * (np.pi/lam/z) * (X0m**2 + Y0n**2))
        f_mn = source * phase_0
        F_pq = np.fft.fftshift(np.fft.fft2(f_mn))
        
        # after fourier transform
        hologram_resolution = lam * z / N / source_resolution
        x1p = hologram_resolution * np.arange(-N//2, N//2)
        y1q = hologram_resolution * np.arange(-N//2, N//2)
        X1p, Y1q = np.meshgrid(x1p, y1q)
        
        phase_1 = np.exp(1j * 2 * np.pi * z / lam) * np.exp(1j*(np.pi/lam/z) * (X1p**2 + Y1q**2))
        fresnel = (1/1j/lam/z) * phase_1 * F_pq
        fresnel = fresnel * source_resolution * source_resolution
        
        return fresnel, hologram_resolution