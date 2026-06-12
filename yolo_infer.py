from ultralytics import YOLO
import cv2
import sys

model = YOLO("yolov8n.pt")
img_path = sys.argv[1] if len(sys.argv) > 1 else "images/dog.jpg"
results = model(img_path)
annotated = results[0].plot()
cv2.imwrite("outputs/detected.jpg", annotated)
print(f"检测到{len(results[0].boxes)}个目标")

