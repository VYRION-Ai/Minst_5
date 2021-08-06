import torch
from IPython.display import Image, clear_output  # to display images
from IPython.display import YouTubeVideo, display
import yaml
import ast
import streamlit as st
import requests 
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
st.title('My first app')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)
    
download_and_unzip("https://www.dropbox.com/s/0da6paqyt6jg0x1/video2.zip?dl=0")
