
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tanda:" , layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#--USE LOCAL CSS--
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#load_assist
lottie_coding=load_lottieurl("https://lottie.host/32853ad2-755c-4a28-a386-af964fe227cc/YS7QEdUNzb.json")
image_1 = Image.open("images/1st.png")
image_2 = Image.open("images/2nd.png")
#Header Section
st.subheader("Hi, I am Muzammil Hussain :wave:")
st.title("An Electrical Engeneeir From Pakistan")
st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings. ")
st.write("[Learn More >]( https://pythonandvba.com)")


#----WHAT I DO----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            I create this website for fun by using:                                                 
            -Python.                                                                              
            -Streamlit.                                                                            
            -Youtube.                                                                           
            -ChatGpt.                                                                              
            -Deepseak.                                                                         

            If You want to make website Use these ways

            """
        )
        st.write("[Here > ](https://youtu.be/A6464U4bPPQ?si=d-csFUM5ecyNc2X1)")

with right_column:
    st_lottie(lottie_coding,height = 300 , key = "coding")
#---progects---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column , text_column = st.columns((1,2))
    with image_column:
        st.image(image_1)
    with text_column:
        st.subheader("Integrate Lottie Animation Inside Your Streamlit App")
        st.write(
            """
            Learn How to Use Lottie files in Your Streamlit App!
            Animation Make Our Web App More Engaging and Fun, and lottie files is easy way to do
            IN This Video I'll Show You , How Exectly Do This
            """
        )
        st.markdown("[Watch Video](https://youtu.be/VqgUkExPvLY?si=lKt-1X2Ju_vksybr)")
with st.container():
    image_column , text_column = st.columns((1,2))
    with image_column:
        st.image(image_2)
    with text_column:
        st.subheader("How to Add Your Contact Form Your Streamlit App")
        st.write(
            """     
            Want To Add Contact From Your Streamlit Website?
            In This Video I Show You How To Add Contact

            """
        )
        st.markdown("[Watch Video](https://youtu.be/VqgUkExPvLY?si=lKt-1X2Ju_vksybr)")





#----Contact-----

with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")
    #docomentation

    contact_form = """
    <form action="https://formsubmit.co/muzammilhuss282@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name="message" placeholder = "Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()