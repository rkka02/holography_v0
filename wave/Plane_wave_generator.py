import numpy as np

class Plane_wave_generator:
    @staticmethod
    def get_wave(shape, lam, resolution, theta):
        N = shape[0]
        ##
        x1p = resolution * np.arange(-N//2, N//2)
        y1q = resolution * np.arange(-N//2, N//2)
        X1p, Y1p = np.meshgrid(x1p, y1q)
        
        reference_wave = np.zeros(shape, dtype=np.complex128)
        reference_wave = np.exp(1j * 2 * np.pi / lam * np.sin(theta) * X1p)
        return reference_wave
