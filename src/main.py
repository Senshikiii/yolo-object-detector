from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.info()

results = model.train(
    data="../data/Blood Cell.v1i.yolov11/data.yaml",
    epochs=30,
    imgsz=640,
    batch=7,
    device='cpu'
)


