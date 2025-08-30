from PIL import Image

def pixelate(image, x, y):
    smaller_size = (x, y)
    #Makes the original image smaller
    smaller_image = image.resize(smaller_size, Image.BILINEAR)

    #Returns image to original image size but with a blocky filter
    new_image = smaller_image.resize(image.size, Image.NEAREST)
    print(f"Image set to: {smaller_size}")

    return new_image