import torch
from IPython.display import Image, clear_output  # to display images
cd yolov5
python detect.py --weights /content/best.pt --img 200 --conf 0.4 --source 0
