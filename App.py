import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(
    page_title='My Demo App',
    page_icon='📁'
)

st.title('Introducing Aviruk')

lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_NP3cUPExy7.json'
st_lottie(load_lottieurl(lottie_url))

md = open('res/profile.md', 'r')
data = md.read()
md.close()

st.markdown(str(data), unsafe_allow_html=True)
