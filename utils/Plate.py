import numpy as np
from PIL import Image

class Plate:
    def __init__(self, shape, resolution):
        # Plate configuration
        self.M, self.N = shape
        if self.M!=self.N:
            raise ValueError('Shape of a plate should be homogeneous')
        self.dp = resolution
        
        # Generate plate
        self.plate = np.zeros((self.N, self.N))

        # Define plate coordinates
        self.plate_x = self.dp * np.arange(-self.N//2, self.N//2)
        self.plate_y = self.dp * np.arange(-self.N//2, self.N//2)
        self.plate_X, self.plate_Y = np.meshgrid(self.plate_x, self.plate_y)
    
    def overlay(self, image, image_resolution):
        # Define the image resolution and coordinates
        m, n = image.shape
        image_x = image_resolution * np.arange(-n//2, n//2)
        image_y = image_resolution * np.arange(-n//2, n//2)
        image_X, image_Y = np.meshgrid(image_x, image_y)
        
        # Calculate the scale ratio between the image and the plate
        scale_ratio = self.dp / image_resolution
        # Resize the image to fit the plate resolution
        scaled_image = np.array(Image.fromarray(image).resize((int(n / scale_ratio), int(n / scale_ratio)), Image.BILINEAR))

        # Calculate the starting indices to place the scaled image at the center of the plate
        start_x = (self.N - scaled_image.shape[0]) // 2
        start_y = (self.N - scaled_image.shape[1]) // 2

        # Overlay the scaled image on the plate
        temp_plate = self.plate.copy()
        temp_plate[start_x:start_x + scaled_image.shape[0], start_y:start_y + scaled_image.shape[1]] = scaled_image
        return temp_plate