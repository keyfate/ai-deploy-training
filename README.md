# YOLOv8 推理部署项目

## 环境要求
- Python 3.10
- ultralytics 8.4+
- onnxruntime
- opencv-python

## 文件说明
| 文件 | 功能 |
|---|---|
| yolo_infer.py | 单张图片推理 |
| batch_infer.py | 批量图片推理 |
| onnx_infer.py | ONNX 推理对比 |
| speed_compare.py | PyTorch vs ONNX 速度对比 |

## 运行方式
```bash
conda activate ai_deploy
cd ~/ai_train
python3 yolo_infer.py

