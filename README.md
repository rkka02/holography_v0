# holography_v0

## Study Record on CGH

**Author:** Rkka

### Abstract
This is a record of the problems I encountered while studying computer-generated holography (CGH) and my attempts to solve them.

### Hologram Calculation
**Q**. (2024.07.25) How to calculate a hologram that successfully reconstructs a desired size and resolution 3D image at a desired distance?

![Hologram](hologram.png)
*Figure 1: Hologram*

### Aliasing
**Q1**. (2024.07.25) When performing a Fourier transform on a hologram, weird aliasing occurs as shown below. Why does this happen, and how can it be fixed?

![Fourier transform of the hologram](hologram_fourier_aliasing.png)
*Figure 2: Fourier transform of the hologram*

**Q2**. (2024.07.25) When simulating hologram reconstruction on a computer, aliasing occurs. Why does this happen, and how can it be fixed?

![Aliasing in reconstructed image](reconstruction_aliasing.png)
*Figure 3: Aliasing in reconstructed image ($\theta = \pi/5$)*
