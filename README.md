# Seed-size-detection
Seed size statistics

#### train
```
python train_rotation.py --data data/voc-new.yaml --cfg models/yolov5s-new.yaml --weights weights/yolov5s.pt --batch-size 32 --epochs 300
```

### detect
```
python detect_rotation.py --source ./data/images --img-size 640 --weights runs/train/exp8/weights/best.pt --conf 0.9
```
