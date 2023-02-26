import streamlit as st
import numpy as np
from matplotlib import image

import math

def mod_img(img, r, g, b):
    size = len(img) * len(img[0])
    rsum, gsum, bsum = np.sum(img, axis=(0, 1))
    rdev, gdev, bdev = r * size - rsum, g * size - gsum, b * size - bsum
    return np.add(img, np.array([rdev, gdev, bdev]))

st.title('Custom RGB')

col1, col2 = st.columns(2)

def handle_image(img_arr):
    redavg, greenavg, blueavg = np.mean(img_array, axis=(0, 1))
    redavg, greenavg, blueavg = int(redavg), int(greenavg), int(blueavg)
    r = col1.slider('Red', 0, 255, value=redavg)
    g = col1.slider('Green', 0, 255, value=greenavg)
    b = col1.slider('Blue', 0, 255, value=blueavg)
    col2.subheader('Original')
    col2.image(img_array / 255)
    if col1.checkbox('Sample original pixel data', key='chk1'):
        col1.write(img_arr[1:3][1:3] / 255)
    modimg = mod_img(img_arr, r, g, b) / 255
    col2.subheader('Modified')
    col2.image(img_arr)
    if col1.checkbox('Sample greyscale pixel data', key='chk2'):
        col1.write(modimg[1:3][1:3])

img_file_buffer = col1.file_uploader('Upload an image', type=['png', 'jpg'])

if img_file_buffer is not None:
    image = image.imread(img_file_buffer)
    img_array = np.array(image)
    if int(img_array.sum() / ( len(img_array)*len(img_array[0])*3 )) <= 1:
        img_array = int(img_array * 255)
    else:
        img_array = img_array
    handle_image(img_array)
