import sys
import os
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
input_dir = sys.argv[1]
exts = (".jpg", ".png")

images = [f for f in os.listdir(input_dir) if f.lower().endswith(exts)]
total = len(images)
total_time = 0

os.makedirs("outputs", exist_ok=True)

for img_name in images:
    img_path = os.path.join(input_dir, img_name)
    start = time.time()
    results = model(img_path)
    elapsed = (time.time() - start) * 1000
    total_time += elapsed
    results[0].save(filename=os.path.join("outputs", img_name))
    print(f"{img_name}: {elapsed:.1f}ms")

print(f"\n共处理 {total} 张图片，平均每张 {total_time / total:.1f}ms")
