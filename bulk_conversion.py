from PIL import Image
import os
path = r'images folder path'
outputpath = r"storage folder path"
l = os.listdir(path)
for i in range(len(l)):
    print(l[i])
    png_image = Image.open(f'{path}\{l[i]}')
    png_image.save(f'{outputpath}\{l[i]}.webp', "webp")

