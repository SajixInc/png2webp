from PIL import Image
import os

# where the images are, that folder path
path = " Images folder  path " # This is a folderpath

# where webp are have to be store
outputpath = "storage path"   #output folderpath

def bluk_converstion():
    l = os.listdir(path)
    for i in range(len(l)):
        print(l[i])
        png_image = Image.open(f'{path}\{l[i]}')
        png_image.save(f'{outputpath}\{l[i]}.webp', "webp")
def image_converstion():
    png_image = Image.open(f'{path}')
    png_image.save(f'{outputpath}.webp', "webp")

image_converstion()

