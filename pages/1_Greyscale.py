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

st.title('Greyscale')

col1, col2 = st.columns(2)

def handle_image(img_arr):
    fn = col1.selectbox(
        'Select greyscale method',
        ('Modified Sigmoid', 'Sigmoid')
    )
    lvl = col1.slider('Set greyscale brightness', 0, 100, value=20) * 5 / 100 if fn == 'Modified Sigmoid' else None
    col2.subheader('Original')
    col2.image(img_array)
    if col1.checkbox('Sample original pixel data', key='chk1'):
        col1.write(img_arr[1:3][1:3])
    gsimd_sq = np.zeros(shape=(len(img_arr), len(img_arr[0]), 3))
    functions = {
        'Modified Sigmoid': squishify,
        'Sigmoid': sigmoid
    }
    for i in range(0, len(img_arr)):
        for j in range(0, len(img_arr[0])):
            gsimd_sq[i,j] = functions[fn](img_arr[i,j].sum(), lvl=lvl)
    col2.subheader('Greyscale')
    col2.image(gsimd_sq)
    if col1.checkbox('Sample greyscale pixel data', key='chk2'):
        col1.write(gsimd_sq[1:3][1:3])

img_file_buffer = col1.file_uploader('Upload an image', type=['png', 'jpg'])

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img_array = np.array(image)
    handle_image(img_array)
