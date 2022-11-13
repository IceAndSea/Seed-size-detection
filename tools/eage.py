import numpy as np
import cv2
import math
import os
import glob
from pathlib import Path
img_formats = ['bmp', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng', 'webp', 'mpo']

#https://blog.csdn.net/loovelj/article/details/90080725

def count_pixel(image_path):
    image = cv2.imread(image_path)  # 读取图片
    length, depth, channels = image.shape
    #图像转化为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 中值滤波
    binary = cv2.medianBlur(gray, 7)

    # 转化为二值图像
    ret, binary = cv2.threshold(binary, 120, 255, cv2.THRESH_BINARY)
    # canny提取轮廓
    canny_image = cv2.Canny(binary, 0, 60, apertureSize=3)

    # 提取轮廓后，拟合外接多边形（矩形）
    contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    maxArea=0
    # 挨个检查看那个轮廓面积最大
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > cv2.contourArea(contours[maxArea]):
            maxArea = i


    minRect=cv2.minAreaRect(contours[maxArea])
    width = int(minRect[1][0])
    height = int(minRect[1][1])
    pixel=0
    if width<1000 or height<1000:
        print('11111111111111111111111')
        print(image_path)
        print('33333333333333333333333')
    else:
        pixel=(210+297)/(width+height)
    min_rect = np.int0(cv2.boxPoints(minRect))
    cv2.drawContours(image, [min_rect], 0, (0, 255, 0), 2)
    cv2.imwrite("rect.png", image)

    return round(pixel,6)

if __name__ == '__main__':
    source='./inference/pic_size/'
    p = str(Path(source).absolute())
    files = glob.glob(os.path.join(p, '*.*'))  # dir
    images = [x for x in files if x.split('.')[-1].lower() in img_formats]
    print(images)
    for i, imgpath in enumerate(images):
        px = count_pixel(imgpath)
        print(px)
