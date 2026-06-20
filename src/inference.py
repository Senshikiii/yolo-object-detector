# i'm pretty sure we need to wrap this script in fastapi
from ultralytics import YOLO

model = YOLO("../runs/detect/train-5/weights/best.pt")

results = model("/Users/yashwinsenshiki/Downloads/istockphoto-1337360537-612x612.jpg", save=True, conf=0.50)




