import torch
from IPython.display import Image, clear_output  # to display images
from IPython.display import YouTubeVideo, display
import yaml
import ast
print(torch.__version__)
cd /content


video = YouTubeVideo("pGgM3c1e8vQ", width=500)
display(video)

cd /yolov5
python detect.py --weights /content/best.pt --img 200 --conf 0.4 --source 0
