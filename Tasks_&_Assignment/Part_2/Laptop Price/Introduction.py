import streamlit as st
import webbrowser
from PIL import Image
import os

path = os.path.dirname(__file__)
picture = path+'/assets/profile_picture.jpg'
image = Image.open(picture)
st.image(image,width=250)

st.title("Hello! I'm :blue[Shivam kumar jha] from Hyderabad, India.")
st.header("I'm Currenlty Pursuing BTech (CSE) with specialization of :orange[AI & ML] at :orange[Malla Reddy University]")
st.subheader('This Streamlit Project is done as a Data Science Intern at :red[Innomatics Research Lab]')
st.subheader('Thank You :green[Innomatics] for giving me this opportunity.')
st.balloons()

linkdin_link ='https://www.linkedin.com/in/shivam-kumar-jha-0022/'
github_link='https://github.com/jhashivam0022'

st.subheader("Linkdin Link - ")
Linkedin=st.button('Linkedin')
if Linkedin:
    webbrowser.open_new_tab(linkdin_link) 

st.subheader("GitHub Link - ") 
Github=st.button('Github')
if Github: 
    webbrowser.open_new_tab(github_link)