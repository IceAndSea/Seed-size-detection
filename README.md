# [Rice seed size measurement using a rotational perception deep learning model](https://www.sciencedirect.com/science/article/pii/S0168169922008912)
# [Computers and Electronics in Agriculture 205: 107583](https://www.sciencedirect.com/science/article/pii/S0168169922008912)

## Seed-size-detection
**Seed-size-detection** is a rice seed size automatic measurement model and tool, which includes a **rotational** perception **deep learning model YOLO-rot** for automatic seed number and size measurement in this work.  

For additional details, we kindly invite you to refer to the Seed-size-detection (YOLO-rot) publication:  
[*<ins>Rice seed size measurement using a rotational perception deep learning model</ins>*](https://www.sciencedirect.com/science/article/pii/S0168169922008912)  

We also offer you the **online service version** of Seed-size-detection. Please visit [*http://www.xhhuanglab.cn/tool/SeedRuler.html*](https://u263790-ad15-4e65cb7d.westc.gpuhub.com:8443/IMSFGM/display.jsp) for more information.


## command
#### train
```
python train_rotation.py --data data/voc-new.yaml --cfg models/yolov5s-new.yaml --weights weights/yolov5s.pt --batch-size 32 --epochs 300
```

#### detect
```
python detect_rotation.py --source ./data/images --img-size 640 --weights runs/train/exp1/weights/best.pt --conf 0.9
```

##YOLO-rot2.0
In 2024, our team continued to release new versions: [*<ins>YOLOrot2.0: a novel algorithm for high-precision rice seed size measurement with real-time processing</ins>*](https://doi.org/10.1016/j.atech.2024.100599)
 Additionally, you can find the YOLOrot2.0 code [*here*](https://github.com/cccccabbage/YOLOrot2.0). And experiments were conducted on the this [*dataset*](https://www.kaggle.com/datasets/cccccabbage/rice370), which consists of 371 rice seed images of total 40,000 seeds.
