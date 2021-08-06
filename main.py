import torch
from IPython.display import Image, clear_output  # to display images
from IPython.display import YouTubeVideo, display
import yaml
import ast
print(torch.__version__)
cd /content
curl -L "https://www.dropbox.com/s/0da6paqyt6jg0x1/video2.zip?dl=0" > video2.zip; unzip video2.zip; 
curl -L "https://www.dropbox.com/s/6zu18goqoqqitlr/best.pt?dl=0" > best.zip; unzip best.zip; 
curl -L "https://www.dropbox.com/s/oovmwed5zotp554/yaml8.zip?dl=0" > yaml8.zip; unzip yaml8.zip; rm yaml8.zip

video = YouTubeVideo("pGgM3c1e8vQ", width=500)
display(video)

cd yolov5
python detect.py --weights /content/best.pt --img 200 --conf 0.4 --source 0
