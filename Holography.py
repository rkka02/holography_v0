import numpy as np
import wave, propagator

class Holography:
    def __init__(self, lam, z0, z1):
        # optical configuration
        self.lam = lam
        self.z0 = z0
        self.z1 = z1
        # parameters for later use
        self.fitted = False
        self.source_resolution = None
        self.hologram_resolution = None
        self.recon_resolution = None
        self.reference_wave_type = None
        self.reference_wave = None

    def reset_resolution(self):
        self.source_resolution = None
        self.hologram_resolution = None
        self.recon_resolution = None

    def fresnel_record(self, source, source_resolution, reference_wave_type='plane', theta=np.pi/10, auto_scaling=False):
        # shape
        M, N = source.shape
        if M!=N:
            raise ValueError('Source shape should be homogeneous')
        
        # resolution setting
        if auto_scaling:
            self.source_resolution = np.sqrt(self.lam*self.z0/N)
            self.hologram_resolution = self.lam * self.z0 / N / self.source_resolution
        else:
            self.source_resolution = source_resolution
            self.hologram_resolution = self.lam * self.z0 / N / self.source_resolution

        # create reference wave
        self.reference_wave_type = reference_wave_type.lower()
        if self.reference_wave_type=='plane':
            self.reference_wave = wave.Plane_wave_generator.get_wave(shape=(N,N), lam=self.lam, resolution=self.hologram_resolution, theta=theta)
        elif self.reference_wave_type=='spherical':
            self.reference_wave = wave.Spherical_wave_generator.get_wave(shape=(N,N), lam=self.lam, resolution=self.hologram_resolution, z=self.z0)
        else:
            raise NotImplementedError('Only plane and spherical wave are supported currently.')
        
        # propagate source field
        fresnel = propagator.Fresnel_propagator.propagate(lam=self.lam, z=self.z0, source=source, source_resolution=self.source_resolution)
        fresnel = (fresnel - fresnel.min())/(fresnel.max() - fresnel.min())
        self.fresnel = fresnel
        hologram = fresnel + 0.5 * self.reference_wave
        
        print('hologram recorded')
        return np.abs(hologram)**2

    def recon(self, recorded_hologram):
        recorded_hologram = recorded_hologram - np.mean(recorded_hologram)
        U0, dx2 = self.propagator.propagate(recorded_hologram)
        self.dx2 = dx2
        
        Gmax = np.max(np.abs(U0))
        Gmin = np.min(np.abs(U0))
        U1 = np.abs(U0)
        U1 = (U1 - Gmin) / (Gmax - Gmin)
        return np.abs(U1)