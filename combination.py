from PIL import Image

def blend_images(image1_path, image2_path, alpha=0.5):
    img1 = Image.open(image1_path).convert("RGBA")
    img2 = Image.open(image2_path).convert("RGBA")
    return Image.blend(img1, img2, alpha)
