import rembg
import PIL
import sys

def clean_background(file):
    inp = PIL.Image.open(file)
    output = rembg.remove(inp)
    output.save('new_img.png')

if __name__ == '__main__':
    input = sys.argv[1]
    clean_background(input)
