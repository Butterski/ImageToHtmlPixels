# author: https://github.com/Butterski
from PIL import Image
import string

im = Image.open('image.png').convert('RGB')

with open("template.html") as t:
    template = string.Template(t.read())

width, height = im.size


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def rgb_of_pixel(x, y):
    r, g, b = im.getpixel((x, y))
    a = rgb2hex(r, g, b)
    return a


def generate_art(option, stretch):
    content = ""
    print("Generating...")
    for y in range(0, height, int(option)):
        content += f'<br>'
        for x in range(0, width, int(option)):
            content += f'<div class="pixel" style="background-color: {rgb_of_pixel(x, y)}"></div>'

    final_output = template.substitute(divs=content, pixels=stretch)
    with open("index.html", "w") as output:
        output.write(final_output)


print("Choose the quality of picture")
print("1 - original quality")
print("Bigger the number = worse quality")
option_input = input()

print("Choose the pixel size")
stretch_input = input()

generate_art(option_input, stretch_input)

print("Done :)")
print("If you inspect the page it may be a bit laggy too!")
