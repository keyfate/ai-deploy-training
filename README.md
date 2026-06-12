# YOLOv8 推理部署项目

一个完整的 YOLOv8 目标检测推理项目，支持单张图片、批量图片、ONNX 部署和速度对比。

## 快速开始（从零到跑通）

```bash
# 1. 下载项目
git clone https://github.com/keyfate/ai-deploy-training.git
cd ai-deploy-training

# 2. 安装依赖
pip install -r requirements.txt

# 3. 准备一张图片放在项目目录下，然后运行
python3 yolo_infer.py 你的图片.jpg
```

> 模型文件 `yolov8n.pt` 已包含在仓库中，不用额外下载。

## 四种运行方式

| 命令 | 作用 | 示例 |
|---|---|---|
| `python3 yolo_infer.py 图片.jpg` | 单张图片检测 | `python3 yolo_infer.py dog.jpg` |
| `python3 batch_infer.py 图片文件夹/` | 批量检测目录下所有图片 | `python3 batch_infer.py images/` |
| `python3 onnx_infer.py` | ONNX 格式推理对比 | 看 PyTorch 和 ONNX 结果是否一致 |
| `python3 speed_compare.py` | 速度对比实验 | PyTorch vs ONNX 各跑 100 次 |

## 性能数据

测试环境：Intel Core i7-14650HX + RTX 4060

| 框架 | 平均推理时间 |
|---|---|
| PyTorch（GPU） | 6.9 ms |
| ONNX Runtime（CPU） | 25.4 ms |

> ONNX 在 CPU 上通常比 PyTorch 快（纯 C++ 推理引擎），但因为本机有 GPU，PyTorch 用 GPU 跑更快。

## 项目结构

```
├── yolo_infer.py        # 单张图片推理（支持命令行参数）
├── batch_infer.py       # 批量图片推理
├── onnx_infer.py        # ONNX 推理验证
├── speed_compare.py     # PyTorch vs ONNX 速度对比
├── requirements.txt     # 依赖清单
├── .gitignore           # 排除大文件（*.onnx / outputs/）
├── images/              # 测试图片
└── docker/              # Docker 打包配置
```

## 踩坑记录

### C 盘爆盘
WSL2 的虚拟硬盘（C 盘 VHDX 文件）只膨胀不缩小。Docker build 失败多次后缓存叠加，VHDX 从 15GB 膨胀到 52GB，导致 C 盘爆满。

**解决：**
```bash
docker system prune -af          # 清理 Docker 缓存
wsl --shutdown                    # 关闭 WSL
# 然后用 diskpart 压缩 VHDX 文件
```

### 端口 22 被封
公司网络封了 GitHub 的 22 端口，git push 报 `Connection refused`。

**解决：** 改用 443 端口连接：
```bash
echo "Host github.com
    Hostname ssh.github.com
    Port 443
    User git" >> ~/.ssh/config
```
