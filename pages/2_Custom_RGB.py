import streamlit as st
import numpy as np
from PIL import Image

import math

def mod_img(img, r, g, b):
    size = len(img) * len(img[0])
    (rsum, gsum, bsum) = np.sum(img, axis=(0, 1))
    (rdif, gdif, bdif) = (
        r - rsum / size,
        g - gsum / size,
        b - bsum / size,
    )
    # make range b/w 0 to 255, int, and adjustments
    (rdif, gdif, bdif) = (
        int(rdif),
        int(gdif),
        int(bdif),
    )
    # st.write((r, g, b))
    # st.write((rsum / size, gsum / size, bsum / size))
    # st.write((rdif, gdif, bdif))
    return np.add(img, np.array([rdif, gdif, bdif]))

st.title('Custom RGB')

col1, col2 = st.columns(2)

def handle_image(img_arr):
    (ravg, gavg, bavg) = np.mean(img_array, axis=(0, 1))
    (ravg, gavg, bavg) = int(ravg), int(gavg), int(bavg)
    r = col1.slider('Red',   0, 255, value=ravg)
    g = col1.slider('Green', 0, 255, value=gavg)
    b = col1.slider('Blue',  0, 255, value=bavg)
    # display original image
    col2.subheader('Original')
    col2.image(img_array)
    # display original RGB sample
    if col1.checkbox('Sample original pixel data', key='chk1'):
        col1.write(img_arr[1:3][1:3])
    # mod image
    modimg = mod_img(img_arr, r, g, b)
    # display modded RGB sample
    if col1.checkbox('Sample mod image pixel data', key='chk2'):
        col1.write(modimg[1:3][1:3])
    # display modded image
    col2.subheader('Modified')
    col2.image(modimg, clamp=True)

img_file_buffer = col1.file_uploader('Upload an image', type=['png', 'jpg'])

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img_array = np.array(image)
    handle_image(img_array)
