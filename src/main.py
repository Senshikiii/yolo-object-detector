from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.info()

results = model.train(data="coco8.yaml", epochs=100, imgsz=640, batch=4, device='cpu')
