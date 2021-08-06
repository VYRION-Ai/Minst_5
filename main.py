import torch
from IPython.display import Image, clear_output  # to display images
from IPython.display import YouTubeVideo, display
import yaml
import ast
import streamlit as st
import requests 
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile




# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os
cwd = os.getcwd()
st.title(cwd)
# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
