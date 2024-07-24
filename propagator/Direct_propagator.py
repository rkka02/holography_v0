import numpy as np

def get_nonzero_index(array):
    nz = []

    for j, y in enumerate(np.nonzero(array)[0]):
        x = np.nonzero(array)[1][j]
        nz.append((x,y))
    
    return nz

def direct_diffraction(s_field, s_coords, o_coords, z, lam):

    k = 2*np.pi/lam
    da = (s_coords[0][0]-s_coords[0][1])**2

    ox = o_coords[0]
    oy = o_coords[1]
    oX, oY = np.meshgrid(ox, oy)

    s_index = get_nonzero_index(s_field)
    result = np.zeros(oX.shape)
    
    for index in s_index:
        sx = s_coords[0][index[0]]
        sy = s_coords[1][index[1]]
        r = np.sqrt((sx-oX)**2 + (sy-oY)**2 + z**2)
        u = s_field[index[1], index[0]]
        
        result = result + u * (1/r) * np.exp(1j*k*r) * (z/r) * (1 + 1j/(k*r)) * da

    result = result * (1/(1j*lam))

    return result