from PIL import Image
import math
import sys

try:
    file = sys.argv[1]
except:
    print("bruh")
    quit()


im = Image.open(file)
im = im.convert("HSV")

im = im.transpose(Image.FLIP_TOP_BOTTOM)

im_size = im.size
desmos_size = (32,32)

step = (int(im_size[0]/desmos_size[0]),int(im_size[1]/desmos_size[1]))

colors = []
for r in range(desmos_size[1]):
    for c in range(desmos_size[0]):
        colors.append(im.getpixel((r * step[0],c * step[1])))

def Floor(x):
    return math.floor(x*100)/100

mid = ",".join([f'\\left({Floor(360*(c[0]/255))},{Floor(c[1]/255)},{Floor(c[2]/255)}\\right)' for c in colors])
output = "\\left["+mid+"\\right]"

print(output)