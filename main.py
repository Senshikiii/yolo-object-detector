from ultralytics import YOLO

model = YOLO("yolo11.pt")

model.info()

results = model.train(data="", epochs=30, imgsz=640, batch=32)
