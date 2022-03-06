import streamlit as st
import numpy as np
from PIL import Image

global saved_image

st.title("Book Detection Camera Module")


st.button('start Camera')
picture = st.camera_input("Take a picture")
if picture:
     saved_image = st.image(picture, channels="BGR")
