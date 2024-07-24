import numpy as np

class Padder:
    def pad_image(image):
        h, w = image.shape
        new_h = max(2**(int(np.log2(h))+1), 2**(int(np.log2(w))+1))
        new_w = new_h
        shift_h, shift_w = (new_h-h)//2, (new_w-w)//2
            
        padded_image = np.zeros((new_h, new_w))
        padded_image[0:h, 0:w] = image
        padded_image = np.roll(padded_image, shift=shift_h, axis=0)
        padded_image = np.roll(padded_image, shift=shift_w, axis=1)

        return padded_image