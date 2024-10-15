import interpolation as interp
import geometric_transform as geom
import intensity_transform as inten
import isolate as iso
import noise
import filters

class Image:
    """
        A class to allow for chaining of image transformations.
        We may store other metadata 
        here in the future.
    """

    def __init__(self, img):
        """
            Initialize the image object.
        """
        self.img = img

    def linear_interpolation(self):
        """
            Linear interpolation between the pixels of the image.
        """
        interp.linear_interpolation(self.img)
        return self
    
    def bilinear_interpolation(self):
        """
            Bilinear interpolation between the pixels of the image.
        """
        interp.bilinear_interpolation(self.img)
        return self

    def render(self):
        """
            Render the image.
        """
        pass