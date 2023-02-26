import streamlit as st

md = open('res/profile.md', 'r')
data = md.read()
md.close()

st.markdown(str(data))
