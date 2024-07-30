import numpy as np

class Spherical: 
    def get_wave(shape, lam, resolution, z):
        N = shape[0]

        x = resolution * np.arange(-N//2, N//2)
        y = resolution * np.arange(-N//2, N//2)
        X, Y = np.meshgrid(x, y)
        
        # prevent spherical wave aliasing
        spherical_wave_aliasing_limit = z/np.sqrt((2*resolution/lam)**2 - 1)
        reference_wave = np.zeros(shape, dtype=np.complex128)
        reference_wave = np.exp(1j * np.pi * (X**2 + Y**2) / (lam * z))
        reference_wave[np.abs(X)>=spherical_wave_aliasing_limit] = 0
        reference_wave[np.abs(Y)>=spherical_wave_aliasing_limit] = 0
        
        return reference_wave
