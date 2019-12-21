from PIL import Image, ImageDraw, ImageFont
import os

print('enter dir of images you wish to watermark')
directory = input()
os.chdir(directory)
print('enter watermark text')
text = input()
print('enter font .ttf')
fontentry = input()
print('enter text size')
fontsize = int(input())
print('enter margin')
margin = int(input())

print('watermarking photos')
for image in os.listdir(directory):
    try:
        photo = Image.open(image)
        width, height = photo.size
        watermark = ImageDraw.Draw(photo)
        font = ImageFont.truetype(fontentry, fontsize)
        textwidth, textheight = watermark.textsize(text, font)
        x = width - textwidth - margin
        y = height - textheight - margin
        watermark.text((x,y), text, font=font)
        photo.save(image)
    except:
        for image in os.listdir(directory):
            print('will not open ' + image + '. not an image file?')


