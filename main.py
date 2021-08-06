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


def download_url(url, save_path):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
            
            
download_url("https://www.dropbox.com/s/0da6paqyt6jg0x1/video2.zip?dl=0","Minst_5/models")
