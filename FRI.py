from PIL import Image
import os, sys, csv
import numpy as np
from collections import Counter
import pandas as pd
from random import shuffle
import random
from keras.preprocessing.image import ImageDataGenerator



path = "/Users/sharmarochan/Desktop/extracted files/resized_images/"
dirs = os.listdir( path )
dirs_array = np.array(dirs)
dirs_array_sort = np.sort(dirs_array)
# print(dirs_array_sort)



def resize():
    with open('/Users/sharmarochan/Desktop/extracted files/num_images_temp.csv','w') as f:
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


def shuffel_csv():
    data = pd.read_csv('/Users/sharmarochan/Desktop/extracted files/num_images.csv')
    data.reset_index(drop=True)
    print(data)


# shuffel_csv()


def dataaugumentation():

    datagen = ImageDataGenerator( rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest')

    for item in dirs_array_sort:

        im = Image.open(path + item)
        x = x.reshape((1,) + x.shape)
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir='preview', save_prefix='augumented', save_format='jpg'):
            i += 1
            if i > 20:
                break

dataaugumentation()