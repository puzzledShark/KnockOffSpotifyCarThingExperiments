from PIL import Image
import struct

def convert_to_rgb565(image):
    """Convert an image to RGB565 format."""
    width, height = image.size
    rgb565_data = bytearray()

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
            rgb565_data.extend(struct.pack('>H', rgb565))

    return rgb565_data

def resize_and_crop(image_path, size):
    with Image.open(image_path) as img:
        # Resize the image while maintaining aspect ratio
        img.thumbnail((size[0], size[1]), Image.ANTIALIAS)
        
        # Calculate cropping box
        left = (img.width - size[0]) / 2
        top = (img.height - size[1]) / 2
        right = (img.width + size[0]) / 2
        bottom = (img.height + size[1]) / 2
        
        # Crop the image to the desired size
        img = img.crop((left, top, right, bottom))
        
        return img
    
def processImage(image_path, size):
    image = resize_and_crop(image_path, size)
    processedImage = image.convert('RGB')
    finalImage = convert_to_rgb565(processedImage)
    return finalImage
