import os, sys, csv, cv2
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import warnings
from PIL import Image
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input

from matplotlib.pyplot import imshow


from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten


path = "/Users/sharmarochan/Desktop/extracted files/augumented_image/"
test_path = "/Users/sharmarochan/Desktop/extracted files/resized_images/"


dirs = os.listdir( path )
dirs_array = np.array(dirs)
dirs_array_sort = np.sort(dirs_array)


def path_csv():
    with open('/Users/sharmarochan/Desktop/extracted files/image_path_lable.csv','w') as f:
        writer = csv.writer(f)
        lable =1
        image = 0
        val_store = "Barking_deer"


        for item in dirs_array_sort:

            if not item.startswith('.') and item != 'Thumbs.db':
                image = image + 1

                par1, par2, par3,par4,par5= item.rsplit('_', 4)
                im = path+item

                if val_store != par1:
                    lable = lable + 1
                    val_store = par1

            if not item.startswith('.') and item != 'Thumbs.db':
                if os.path.isfile(path + item):
                    # im = Image.open(path + item)
                    writer.writerow([im, lable])

# path_csv()



def extract_pixels_from_jpg():

    with open('image_path_lable.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            p = row[0]
            p1, p2 = p.split(',')  #p1 is path, # p2 is lable
            print(p1)
            img_path = '/Users/sharmarochan/Desktop/extracted files/augumented_image/Barking_deer_agu_0_0_0.jpg'

            img = image.load_img(img_path, target_size=(256, 256))
            imshow(img)
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            print (x.shape)

            break

extract_pixels_from_jpg()



def dataaugumentation():

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category = FutureWarning)

    datagen = ImageDataGenerator(featurewise_center=True, featurewise_std_normalization=True, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2, horizontal_flip=True)
    image_per = 0


    for item in dirs_array_sort:

        if not item.startswith('.') and item != 'Thumbs.db':

            image_per = image_per + 1
            print("image: ", image_per)

            par1, par2 = item.rsplit('_', 1)

            im = load_img(path + item)
            x = img_to_array(im)
            x = x.reshape((1,) + x.shape)
            i = 0

            for batch in datagen.flow(x, batch_size=1, save_to_dir='augumented_image', save_prefix=par1 + '_agu_' + str(i), save_format='jpg'):
                i += 1
                if i > 15:
                    break

# dataaugumentation()



# def createModel():
