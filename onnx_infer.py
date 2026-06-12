from ultralytics import YOLO
import onnxruntime as ort
import numpy as np
import cv2

img = cv2.imread("images/dog.jpg")

model_pt = YOLO("yolov8n.pt")
res_pt = model_pt(img)[0]

model_onnx = ort.InferenceSession("yolov8n.onnx")
input_name = model_onnx.get_inputs()[0].name
img_resized = cv2.resize(img, (640, 640))
img_input = img_resized.transpose(2,0,1)[None]/255.0
res_onnx = model_onnx.run(None,{input_name : img_input.astype(np.float32)})

print(f"PyTorch 检测到{len(res_pt.boxes)}个目标")
for box in res_pt.boxes:
    print(f"{box.cls.item()}: {box.xyxy.tolist()} conf={box.conf.item():.2f}")

print(f"ONNX 输出 shape: {res_onnx[0].shape}")
