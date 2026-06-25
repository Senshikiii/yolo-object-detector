# i'm pretty sure we need to wrap this script in fastapi

from fastapi.responses import FileResponse
from ultralytics import YOLO
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io


# we've imported all the imports, so now we make an instance of the object and then just load the model and wrap things up?? 

app = FastAPI()

model = YOLO("../runs/detect/train-5/weights/best.pt")

OUTPUT_PATH = "static_prediction.jpg"

@app.post("/upload_image")
async def receive_and_process(file: UploadFile = File(...)): # an ellipsis is smth like a condition where a file or anything is strictly needed
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes))

    results = model(img, conf=0.50)   # .plot() returns a raw array tho (numbers representing rgb pixel coords)
    plotted_array = results[0].plot() # since YOLO outputs the a python list containing the outputs, but i'm not so sure abt it, like the list has an index of 1 but we use [0] to pull just the single specific image?
    output_img = Image.fromarray((plotted_array))  # it gets turned to  a PIL object, and some img manipulation thing goes on
    output_img.save(OUTPUT_PATH)

    return {
        "filename": file.filename,
        "total_detections": len(results[0].boxes), # a method used to get the length of the boxes (not a builtin python method btw)
        "message": "Image processed!"
    }

@app.get("/image")
async def send_back_image():
    return FileResponse(path=OUTPUT_PATH, media_type="image/jpeg")
