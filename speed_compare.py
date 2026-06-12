import time
import cv2
from ultralytics import YOLO
import onnxruntime as ort
import numpy as np

img = cv2.imread("images/dog.jpg")
img_resized = cv2.resize(img, (640, 640))

model_pt = YOLO("yolov8n.pt")
_ = model_pt(img)
pt_times = []
for _ in range(100):
    start = time.time()
    model_pt(img)
    pt_times.append((time.time() - start) * 1000)
pt_avg = sum(pt_times) / len(pt_times)

session = ort.InferenceSession("yolov8n.onnx")
input_name = session.get_inputs()[0].name
img_input = img_resized.transpose(2, 0, 1)[None] / 255.0
img_input = img_input.astype(np.float32)
_ = session.run(None, {input_name: img_input})
onnx_times = []
for _ in range(100):
    start = time.time()
    session.run(None, {input_name: img_input})
    onnx_times.append((time.time() - start) * 1000)
onnx_avg = sum(onnx_times) / len(onnx_times)

print(f"| 框架 | 平均推理时间 |")
print(f"|---|---|")
print(f"| PyTorch | {pt_avg:.1f} ms |")
print(f"| ONNX Runtime | {onnx_avg:.1f} ms |")

