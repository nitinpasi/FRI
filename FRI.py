from PIL import Image
import os, sys, csv
import numpy as np
from collections import Counter

path = "/Users/sharmarochan/Desktop/extracted files/images_together/"
dirs = os.listdir( path )
dirs_array = np.array(dirs)
dirs_array_sort = np.sort(dirs_array)
# print(dirs_array_sort)



def resize():
    with open('/Users/sharmarochan/Desktop/extracted files/num_images.csv','w') as f:
        writer = csv.writer(f)
        lable =1
        image = 0
        val_store = "Barking_deer"



        for item in dirs_array_sort:

            if not item.startswith('.') and item != 'Thumbs.db':
                image = image + 1

                par1, par2 = item.rsplit('_', 1)

                if val_store != par1:
                    lable = lable + 1

                val_store= par1
                print(image)


            if not item.startswith('.') and item != 'Thumbs.db':
                if os.path.isfile(path + item):
                    im = Image.open(path + item)
                    imResize = im.resize((256, 256), Image.ANTIALIAS)
                    value = np.array(imResize)
                    writer.writerow([value, lable])


resize()