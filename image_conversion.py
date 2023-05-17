from PIL import Image
import os

# where the images are, that folder path
path = r"C:\Users\LT-VFY-HP-112021-031\Pictures\test\Screenshot 2022-02-22 165322.png" # This is a folder path

# where webp are have to be store
outputpath = r"C:\Users\LT-VFY-HP-112021-031\Pictures\test\Output"   #output folder path

# For Bulk Conversion
# --------------------------
# def bluk_conversion():
#     l = os.listdir(path)
#     for i in range(len(l)):
#         print(l[i])
#         png_image = Image.open(f'{path}\{l[i]}')
#         png_image.save(f'{outputpath}\{l[i]}.webp', "webp")
# --------------------------

# for single image conversion
def image_conversion():
    png_image = Image.open(f'{path}')
    png_image.save(f'{outputpath}.webp', "webp")

image_conversion()

