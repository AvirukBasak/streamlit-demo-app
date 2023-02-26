import streamlit as st

st.set_page_config(
    page_title='My Demo App',
    page_icon='📁'
)

md = open('res/profile.md', 'r')
data = md.read()
md.close()

st.markdown(str(data), unsafe_allow_html=True)
