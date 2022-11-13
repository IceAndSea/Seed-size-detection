import os
import xml.etree.ElementTree as ET
import math
import matplotlib.pyplot as plt
import numpy as np
import glob
from pathlib import Path

# from matplotlib import rcParams
# config = {
#     "font.family":'serif',
#     "font.size": 24,
#     "mathtext.fontset": 'stix',
# #     "font.serif": ['SimSun'],
#
# }
# rcParams.update(config)

plt.rc('font',family='Times New Roman')


x_list=[]
y_list=[]
w_list=[]
h_list=[]
angle_list = []   # 存储角度的列表

# Plotting functions ---------------------------------------------------------------------------------------------------
def hist2d(x, y, n=100):
    # 2d histogram used in labels.png and evolve.png
    x=np.array(x)
    y=np.array(y)
    xedges, yedges = np.linspace(x.min(), x.max(), n), np.linspace(y.min(), y.max(), n)
    hist, xedges, yedges = np.histogram2d(x, y, (xedges, yedges))
    xidx = np.clip(np.digitize(x, xedges) - 1, 0, hist.shape[0] - 1)
    yidx = np.clip(np.digitize(y, yedges) - 1, 0, hist.shape[1] - 1)
    return np.log(hist[xidx, yidx])

# 读取xml文件，存储其中的angle值
def read_xml(xml_file):
    """
    读取xml文件，找到角度并存储进列表
    :param xml_file:xml文件的路径
    :return:
    """
    tree = ET.parse(xml_file)
    objs = tree.findall('object')
    for ix, obj in enumerate(objs):
        robndbox = obj.find('robndbox')
        if robndbox is not None:
            x_label = float(robndbox.find('cx').text)
            y_label = float(robndbox.find('cy').text)
            w_label = float(robndbox.find('w').text)
            h_label = float(robndbox.find('h').text)
            x_list.append(x_label)
            y_list.append(y_label)
            w_list.append(w_label)
            h_list.append(h_label)

            angle = float(robndbox.find('angle').text)
            angle = angle * 180 / math.pi   # 弧度转化为角度
            angle_list.append(angle)        # 添加进列表

def plt_hist(angle_list):
    save_dir = str(Path('./zjf_plots_labels').absolute())
    plt.figure(figsize=(12, 12))
    # 绘制直方图
    plt.hist(x=angle_list,  # 指定绘图数据
    bins = 30,  # 指定直方图中条块的个数
    color = 'steelblue',  # 指定直方图的填充色
    edgecolor = 'black')  # 指定直方图的边框色
    # 添加x轴和y轴标签
    plt.xlabel('Angle', fontdict={'size': 28})
    plt.ylabel('Object_num ( all:%d )'%(len(angle_list)), fontdict={'size': 28})
    # 添加标题
    plt.title('xml-angle',fontsize=28)
    # 设置横坐标刻度和起始
    my_xticks = np.arange(0,185,15)
    plt.xticks(my_xticks,fontproperties='Times New Roman',size=24)
    # 显示图形
    # plt.show()
    plt.savefig(Path(save_dir) / 'labels_angle.png', dpi=200)
    plt.close()
def plot_labels(x_list,y_list,w_list,h_list):
    save_dir = str(Path('./plots_labels').absolute())
    fig,ax=plt.subplots(1,2,figsize=(8,8),tight_layout=True)
    ax=ax.ravel()
    # ax[0].hist(c,bins=np.linspace(0,1,1+1)-0.5,rwidth=0.8)
    # ax[0].set_xlabel('classes')
    ax[0].scatter(x_list,y_list,c=hist2d(x_list,y_list,90),cmap='jet')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[1].scatter(w_list, h_list, c=hist2d(w_list, h_list, 90), cmap='jet')
    ax[1].set_xlabel('width')
    ax[1].set_ylabel('height')
    plt.savefig(Path(save_dir)/'labels.png',dpi=200)
    plt.close()
def plot_labels_xy(x_list,y_list):
    save_dir = str(Path('./zjf_plots_labels').absolute())
    plt.figure(figsize=(12, 12))
    plt.scatter(x_list, y_list, c=hist2d(x_list, y_list, 90), cmap='jet')
    plt.xlabel('x', fontdict={'size': 28})
    plt.ylabel('y', fontdict={'size': 28})
    plt.yticks(size=28)
    plt.xticks(size=28)
    plt.savefig(Path(save_dir) / 'labels_xy.png', dpi=200)
    plt.close()

def plot_labels_wh(w_list,h_list):
    save_dir = 'zjf_plots_labels'
    plt.figure(figsize=(12, 12))
    plt.scatter(w_list,h_list, c=hist2d(w_list,h_list, 90), cmap='jet')
    plt.xlabel('width', fontdict={'size': 28})
    plt.ylabel('height', fontdict={'size': 28})
    plt.yticks(size=28)
    plt.xticks(size=28)
    plt.savefig(Path(save_dir) / 'labels_wh.png', dpi=200)
    plt.close()

if __name__ == '__main__':
    source = './zjf_datasets/first_anns/'
    p = str(Path(source).absolute())
    files = glob.glob(os.path.join(p, '*.*'))  # dir

    # xmls_dir = 'E:/Projects/xmls_origin'
    # xmls = os.listdir(xmls_dir)
    for xml in files:
        read_xml(xml) # 读取一遍xml文件，存储角度值

    plt_hist(angle_list)
    plot_labels_xy(x_list,y_list)
    plot_labels_wh(w_list, h_list)