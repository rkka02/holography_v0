import numpy as np

class Spherical_wave_generator: 
    def get_wave(self, shape, lam, resolution, z):
        N = shape[0]

        ##
        x1p = resolution * np.arange(-N//2, N//2)
        y1q = resolution * np.arange(-N//2, N//2)
        X1p, Y1q = np.meshgrid(x1p, y1q)
        
        reference_wave = np.zeros(shape, dtype=np.complex128)
        reference_wave = np.exp(1j * np.pi * (X1p**2 + Y1q**2) / (lam * z0))
        return reference_wave
