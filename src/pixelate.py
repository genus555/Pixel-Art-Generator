from PIL import Image

def pixelate(image):
    smaller_size = (image.x, image.y)
    #Changes the original image size
    smaller_image = image.image.resize(smaller_size, Image.BILINEAR)

    #Returns image to original image size but with a blocky filter
    new_image = smaller_image.resize(image.image.size, Image.NEAREST)
    print(f"Image set to: {smaller_size}")

    return new_image