# Seed-size-detection
Seed size statistics

#### train
```
python train_rotation.py --data data/voc-seed.yaml --cfg models/yolov5s-seed.yaml --weights weights/yolov5s.pt --batch-size 32 --epochs 200
```

### detect
```
python detect_rotation.py --source ./data --img-size 640 --weights runs/train/exp1/weights/best.pt --conf 0.45 --save-txt
```
