import streamlit as st

st.header('Demo Echo App')

def txt_changed():
    st.write('', txt)

txt = st.text_input('Input',
    placeholder = 'Enter any text',
    on_change = txt_changed
)
