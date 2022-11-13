import os
import random
from shutil import copyfile

image_dir='../zjf_datasets/size_y/rice_size370/first_images/'
list_imgs = os.listdir(image_dir)
probo = random.randint(1, 100)
annotation_dir='../zjf_datasets/size_y/rice_size370/first_txts/'

workdir = '../VOCdevkit/'
imgages = os.path.join(workdir, 'images_ori')
labels = os.path.join(workdir, 'labels_ori')
train_img = os.path.join(imgages, 'train')
val_img = os.path.join(imgages, 'val')
train_label = os.path.join(labels, 'train')
val_label = os.path.join(labels, 'val')
for d in [imgages, labels, train_img, val_img, train_label, val_label]:
    if not os.path.exists(d):
        os.mkdir(d)

for i in range(0, len(list_imgs)):
    path = os.path.join(image_dir, list_imgs[i])
    if os.path.isfile(path):
        image_path = image_dir + list_imgs[i]
        voc_path = list_imgs[i]
        (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
        (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
        label_name = nameWithoutExtention + '.txt'
        label_path = os.path.join(annotation_dir, label_name)
    probo = random.randint(1, 100)
    print("Probobility: %d" % probo)
    if (probo < 80):  # train dataset
        # print(train_img)
        # print(train_img + voc_path)
        copyfile(image_path, train_img + '/'+voc_path)
        copyfile(label_path, train_label + '/'+label_name)
    else:  # test dataset
        copyfile(image_path, val_img + '/'+voc_path)
        copyfile(label_path, val_label + '/'+label_name)
