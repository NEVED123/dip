from PIL import Image
import numpy as np

def to_matrix(img_path):
    img = Image.open(img_path).convert('L')
    pixels = list(img.getdata())
    width, height = img.size
    matrix = [pixels[i * width:(i + 1) * width] for i in range(height)]
    return np.array(matrix)

def print_matrix(img):
    for row in img:
        print(" ".join(map(str, row)))

def render_image(img, name = 'Image'):
    m = len(img)
    n = len(img[0])
    image = Image.new('L', (n, m))
    
    for y in range(m):
        for x in range(n):
            image.putpixel((x,y), img[y][x].item())

    image.show(title = name)