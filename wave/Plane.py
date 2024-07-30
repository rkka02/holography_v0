import numpy as np

class Plane:
    @staticmethod
    def get_wave(shape, resolution, lam, theta_degree):
        N = shape[0]
        ## check whether theta exceeds diffraction limit (to prevent aliasing)
        theta_limit = np.arcsin(lam/2/resolution) * 180/np.pi
        if theta_degree > theta_limit:
            raise ValueError('Theta exceeds diffraction limit. Maximum possible theta in this case is : ' + str(theta_limit) + ' (degree)')
        
        x1p = resolution * np.arange(-N//2, N//2)
        y1q = resolution * np.arange(-N//2, N//2)
        X1p, _ = np.meshgrid(x1p, y1q)
        
        reference_wave = np.zeros(shape, dtype=np.complex128)
        reference_wave = np.exp(1j * 2 * np.pi / lam * np.sin(theta_degree*np.pi/180) * X1p)
        return reference_wave
