from PIL import Image

def resize_image(image_path, size):
    img = Image.open(image_path)
    return img.resize(size)
