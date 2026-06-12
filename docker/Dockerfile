FROM python:3.10-slim

# 装OpenCV需要的系统库
RUN apt update && apt install -y libxcb-shm0 libxcb1 libxcb-randr0 libxcb-xfixes0 libxcb-shape0 libgl1 --no-install-recommends && rm -rf /var/lib/apt/lists/*

# 装YOLO依赖（用清华源）
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ultralytics

# 复制模型和推理脚本
COPY yolov8n.pt .
COPY docker/infer.py .

ENTRYPOINT ["python", "infer.py"]
