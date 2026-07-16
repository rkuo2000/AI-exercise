# Train YOLO26 with Tank dataset

import kagglehub
dataset_path = kagglehub.dataset_download('rkuo2000/tank-by-s-danish')
print(dataset_path)

import os
print(os.listdir(dataset_path))

from ultralytics import YOLO
model = YOLO("yolo26n.pt")

results = model.train(data="./tanks.yaml", epochs=100, imgsz=640)

testfile = os.path.join(dataset_path, 'test', 'images', 'image_88_jpg.rf.1db53a7e14e975a31f4d01c2b9e4c5db.jpg')
results = model(testfile)
results[0].show()
