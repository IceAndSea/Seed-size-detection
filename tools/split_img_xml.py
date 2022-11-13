
'''
将原始数据集中的xml文件和图像文件进行分开，并且分开保存
'''
import os
from PIL import Image
import shutil
import sys

from shutil import copyfile

#转变图片格式的函数，将source_path路径下的图片转化为types格式
def changepng(source_path,png_path, xml_path,txt_path):
    image_list=os.listdir(source_path)
    files = [os.path.join(source_path,_) for _ in image_list]
    for index,jpg in enumerate(files):
        (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(jpg))
        if ".txt" in jpg:
            # (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(jpg))
            label_name = nameWithoutExtention + extention
            copyfile(jpg, txt_path + label_name)
        elif ".xml" in jpg:
            # (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(jpg))
            label_name = nameWithoutExtention + '.xml'
            copyfile(jpg, xml_path + label_name)

        else:
            label_name = nameWithoutExtention + extention
            copyfile(jpg, png_path + label_name)
    sys.stdout.write('Convert Over!\n')
    sys.stdout.flush()

if __name__ == '__main__':

    # 创建固定格式的数据文件目录
    wd = os.getcwd()
    # images_dir = 'datasets\\JPEGImages\\' #保存图片文件夹
    # annotations_dir = 'datasets\\Annotations\\'#保存xml文件夹
    images_dir = '../zjf_datasets/size_y/rice_size370/first_images/'  # 保存图片文件夹
    annotations_dir = '../zjf_datasets/size_y/rice_size370/first_anns/'  # 保存xml文件夹
    txt_dir='../zjf_datasets/size_y/rice_size370/first_txts/'
    if os.path.exists(images_dir):
        shutil.rmtree(images_dir)
    os.makedirs(images_dir)
    if os.path.exists(annotations_dir):
        shutil.rmtree(annotations_dir)
    os.makedirs(annotations_dir)
    if os.path.exists(txt_dir):
        shutil.rmtree(txt_dir)
    os.makedirs(txt_dir)
    # 将图片转化为png格式
    source_path = os.path.join(wd, "../zjf_datasets/size_y/rice_size370/first_datasets/")#原始数据集
    changepng(source_path, images_dir, annotations_dir,txt_dir)