import streamlit as st
import numpy as np
from PIL import Image

import math

def ReLU(x, lvl=None):
    return x * (x > 0)

def sigmoid(x, lvl=None):
  return 1 / (1 + math.exp(-x))

def squishify(x, lvl=1):
    return sigmoid(x -lvl)

def mean_div(x, lvl=None):
    return x / 3

st.title('Greyscale')

col1, col2 = st.columns(2)

def handle_image(img_arr):
    # select function
    fn = col1.selectbox(
        'Select greyscale method',
        ('Modified Sigmoid', 'Sigmoid', 'Average')
    )
    # select greyscale brightness
    lvl = col1.slider('Set greyscale brightness', 0, 100, value=30) * 5 / 100 if fn == 'Modified Sigmoid' else None
    # display original image
    col2.subheader('Original')
    col2.image(img_array)
    # display original RGB sample
    if col1.checkbox('Sample original pixel data', key='chk1'):
        col1.write(img_arr[1:3][1:3])
    # greyscale image
    gsimd_sq = np.zeros(shape=(len(img_arr), len(img_arr[0]), 3))
    # a list of functions available
    functions = {
        'Modified Sigmoid': squishify,
        'Sigmoid': sigmoid,
        'Average': mean_div
    }
    # bring down the values to range of 0 to 1
    img_arr = img_arr / 255
    # convert to greyscale
    for i in range(0, len(img_arr)):
        for j in range(0, len(img_arr[0])):
            gsimd_sq[i,j] = functions[fn](img_arr[i,j].sum(), lvl=lvl)
    # bring up the values to range of 0 to 255
    gsimd_sq = (gsimd_sq * 255).astype(int)
    # display greyscale image
    col2.subheader('Greyscale')
    col2.image(gsimd_sq)
    # display greyscale RGB sample
    if col1.checkbox('Sample greyscale pixel data', key='chk2'):
        col1.write(gsimd_sq[1:3][1:3])

img_file_buffer = col1.file_uploader('Upload an image', type=['png', 'jpg'])

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img_array = np.array(image)
    handle_image(img_array)
