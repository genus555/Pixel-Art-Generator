from PIL import Image

class ImageObj:
    def __init__(self, image, image_name, x, y, pixel_image=''):
        self.image = image
        self.image_name = image_name
        self.x = x
        self.y = y
        self.pixel_image = pixel_image
