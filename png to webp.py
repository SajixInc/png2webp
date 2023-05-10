from PIL import Image
import os
path = r'C:\Users\vivif\slip_voter_images' # This is a folderpath
outputpath = r"C:\Users\vivif\PycharmProjects\pythonProject\webp_images"   #output folderpath
l = os.listdir(path)    #
for i in range(len(l)):
    print(l[i])
    png_image = Image.open(f'{path}\{l[i]}')
    png_image.save(f'{outputpath}\{l[i]}.webp', "webp")