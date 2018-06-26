from PIL import Image
import os, sys, csv
import numpy as np
from collections import Counter

path = "/Users/sharmarochan/Desktop/extracted files/resized_images/"
dirs = os.listdir( path )
dirs_array = np.array(dirs)
dirs_array_sort = np.sort(dirs_array)
# print(dirs_array_sort)



name = []
for sp in dirs_array_sort:
    if not sp.startswith('.') and sp != 'Thumbs.db':
        part1, part2= sp.rsplit('_', 1)
        name.append(part1)




unique_name = []
for x in name:
    # check if exists in unique_list or not
    if x not in unique_name:
        unique_name.append(x)


unique_count = []
for unique in unique_name:
    countt = name.count(unique)
    unique_count.append(countt)


print(unique_name,unique_count)


def resize():
    with open('/Users/sharmarochan/Desktop/extracted files/num_data_resized_images.csv','w') as f:
        writer = csv.writer(f)
        lable =0
        loop_check = 0
        pos =0

        for item in dirs_array_sort:
            while True:
                if loop_check == unique_count[pos]:
                    lable = lable + 1
                    print("lable",lable)
                    pos = pos + 1
            loop_check = loop_check + 1

            if not item.startswith('.') and item != 'Thumbs.db':
                if os.path.isfile(path + item):
                    im = Image.open(path + item)
                    imResize = im.resize((256, 256), Image.ANTIALIAS)
                    value = np.array(imResize)
                    writer.writerow([value, lable])


'''

        for item,loop in zip(dirs_array_sort,unique_count):
            loop_check = loop_check + 1
            print("->loop_check:", loop_check)

            if loop == loop_check:
                loop_check = 0
                lable = lable+1
            print("-->lable",lable)


            if not item.startswith('.') and item != 'Thumbs.db':
                if os.path.isfile(path+item):
                    im = Image.open(path+item)
                    imResize = im.resize((256,256), Image.ANTIALIAS)
                    value = np.array(imResize)
                    writer.writerow([value,lable])

'''




            # imResize.save(f + ' resized.jpg', 'JPEG', quality=90)








resize()