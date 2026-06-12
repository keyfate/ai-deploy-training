from ultralytics import YOLO
import cv2
import time

model = YOLO("yolov8n.pt")
img = cv2.imread("images/dog.jpg")

# 预热：先随便跑一次，让 CUDA 初始化完成
print("预热中...")
_ = model(cv2.resize(img, (640, 640)))
print("预热完成\n")

for size_name, size in [("640", 640), ("1280", 1280)]:
    img_resized = cv2.resize(img, (size, size))
    times = []
    for _ in range(20):
        start = time.time()
        model(img_resized)
        times.append((time.time() - start) * 1000)
    avg = sum(times) / len(times)
    print(f"Resize: {size}x{size} | 平均耗时: {avg:.1f} ms")
