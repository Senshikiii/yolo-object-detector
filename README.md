# yolo-object-detector

I'm training a YOLO model (v11) on a WBC AND RBC dataset I picked up on roboflow, this not only is a README file but also my roadmap which will have many progressions
I'm gonna be training first but before I begin i'm just gonna explain why i made certain decisions and what i've understood so far. 

## Why YOLO11 specifically?? 
Medical imaging requires the localisation of the objects to be really precise, and since the blood(my dataset) cells could overlap with other cells since they're in huge numbers, an anchor based model isn't really efficient for our specific use-case(it may not match the shapes of the cells)

<img width="841" height="628" alt="Screenshot 2026-06-01 at 21 12 13" src="https://github.com/user-attachments/assets/dea920cd-b651-467b-ab7e-d2c804df8dbf" />



YOLOv11 works really well because it doesn't rely on almost "template" like bounding box shapes like it's predcessors
Unlike two stage detectors, YOLO passes an image to the neural net and both classifies and localises similtaneously
It predicts the confidence scores, coords of the objects detected, and even class probabilites in a single forward pass

Two stage detectors used to rely on region proposal and then classifying it but the process of cropping thousands of "potential" areas where an object could be and then passing it to the neural network is really slow. 
so YOLOv11 is a better architecture for this speific use case


