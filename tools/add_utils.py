import os
from shutil import copyfile
import cv2
import math
from lxml.etree import Element, SubElement, tostring


def move_files(source_path,aim_dir):
    source_list = os.listdir(source_path)
    files = [os.path.join(source_path, _) for _ in source_list]
    for index, source_file in enumerate(files):
        (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(source_file))
        label_name = nameWithoutExtention + extention
        copyfile(source_file, aim_dir + os.sep+label_name)


def txt_xml(img_path,img_name,txt_path,img_txt,xml_path,img_xml):
    #读取txt的信息
    clas=[]
    class_names=['rice']
    img=cv2.imread(os.path.join(img_path,img_name))
    imh, imw = img.shape[0:2]
    # print(txt_path)
    # print(img_txt)
    txt_img=os.path.join(txt_path,img_txt)
    if os.path.exists(txt_img):
        with open(txt_img, "r") as f:
            next(f)
            for line in f.readlines():
                line = line.strip('\n')
                list = line.split(" ")
                # print(list)
                # print(clas)
                clas.append(list)
        node_root = Element('annotation')
        node_folder = SubElement(node_root, 'folder')
        node_folder.text = '1'
        node_filename = SubElement(node_root, 'filename')
        # 图像名称
        node_filename.text = img_name
        node_size = SubElement(node_root, 'size')
        node_width = SubElement(node_size, 'width')
        node_width.text = str(imw)
        node_height = SubElement(node_size, 'height')
        node_height.text = str(imh)
        node_depth = SubElement(node_size, 'depth')
        node_depth.text = '3'
        for i in range(len(clas)):
            x1 = float(clas[i][1])
            y1 = float(clas[i][2])
            w1 = float(clas[i][3])
            h1 = float(clas[i][4])
            # angle1=math.pi+float(clas[i][5])
            # angle1 = float(clas[i][5])
            angle1 = float(clas[i][5]) * math.pi / 180
            # box_xywh = [x1, y1, w1, h1]
            # box_xyxy = rice_xywh2xyxy(box_xywh)

            node_object = SubElement(node_root, 'object')
            node_type = SubElement(node_object, 'type')
            node_type.text='robndbox'
            node_name = SubElement(node_object, 'name')
            node_name.text = str(class_names[int(clas[i][0])])
            node_pose = SubElement(node_object, 'pose')
            node_pose.text = "Unspecified"
            node_truncated = SubElement(node_object, 'truncated')
            node_truncated.text = "truncated"
            node_difficult = SubElement(node_object, 'difficult')
            node_difficult.text = '0'

            node_robndbox = SubElement(node_object, 'robndbox')
            node_cx = SubElement(node_robndbox, 'cx')
            node_cx.text = str(x1)
            node_cy = SubElement(node_robndbox, 'cy')
            node_cy.text = str(y1)
            node_w = SubElement(node_robndbox, 'w')
            node_w.text = str(w1)
            node_h = SubElement(node_robndbox, 'h')
            node_h.text = str(h1)
            node_angle = SubElement(node_robndbox, 'angle')
            node_angle.text = str(angle1)
        xml = tostring(node_root, pretty_print=True)  # 格式化显示，该换行的换行
        img_newxml = os.path.join(xml_path, img_xml)
        file_object = open(img_newxml, 'wb')
        file_object.write(xml)
        file_object.close()
    else:
        print(txt_img+' not exist!')