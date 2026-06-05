#!/usr/bin/env python3
import sys, subprocess, os

print("Python路径:", sys.executable)
print("是否在ai_deploy环境:", "ai_deploy" in sys.executable)

img_dir = "./images"
if os.path.isdir(img_dir):
    imgs = [f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg','.png','.jpeg','.gif','.bmp'))]
    print(f"images/ 下有 {len(imgs)} 张图片")
else:
    print("images/ 目录不存在")

subprocess.run("nvidia-smi", shell=True)
