from openai import OpenAI
import os
import webbrowser
import requests
import streamlit as st
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
st.set_page_config(layout="wide")
st.image('NAU_logo.tif', width=750)
st.header('Department of Global Languages and Cultures', divider='rainbow')
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 30px;"></p>'
st.markdown(new_title, unsafe_allow_html=True)


st.write('****')

st.title('🦜🔗 Image Generator')

prompt_input = st.text_input('Please enter a prompt in the textbox')


def nav_to(url, prompt_input):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    col1, col2 = st.columns([0.1, 0.9])
    with col2:
        st.write(nav_script, unsafe_allow_html=True)
        st.write(prompt_input)

if prompt_input:
    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_input,
        size="1024x1024",
        quality="hd",
        n=1,)

    url = response.data[0].url
    nav_to(url, prompt_input)
