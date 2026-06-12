import sys
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model(sys.argv[1])

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        name = r.names[cls]
        print(f"检测到 {name} (confidence: {conf:.2f})")
print(f"共检测到 {len(results[0].boxes)} 个目标")
