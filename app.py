import streamlit as st

st.header('Demo Echo App')

txt = st.text_input('Input',
    placeholder = 'Enter any text'
)

st.write('', txt)
