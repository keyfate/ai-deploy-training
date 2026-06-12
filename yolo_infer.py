from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")
img_path = "images/dog.jpg"
results = model(img_path,conf=0.8)
annotated = results[0].plot()
cv2.imwrite("outputs/detected.jpg",annotated)
print(f"检测到{len(results[0].boxes)}个目标")
