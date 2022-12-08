import streamlit as st
from PIL import Image
st.set_page_config(page_title="My website",layout="wide")
# adding css

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
# Header
st.subheader("Hello DevOps Training Students")
st.write(" Anael is having his birthday on December 18th!!!!")
# adding videos
video_file = open('vid.mp4', 'rb')
video_bytes = video_file.read()

with st.container():
    st.write("---")
    st.header("My Images")
    st.write("##")
    image_column, text_column = st.columns((1, 2)) 
    with image_column:
        st.image(Image.open("image/anael.jpg"))
        st.image(Image.open("image/anael2.jpg"))
    with text_column:
        st.subheader(" Here comes Anael")
        st.write(" Anael is going to have 3 years in 11 days")
        st.write("Please use the message below to send him a small word")
        st.image(Image.open("image/anael3.jpg"))
        
with st.container():
    st.write("---")
    st.header("My Videos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.subheader("Check videos")
        st.write("Please watch the video to your right, It is how we can create a Virtual machine from the cloud")
    with text_column:
        st.header("My videos")
        st.video(video_bytes)
with st.container():
    st.write("---")
    st.header("Send him an Email here!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/yannickparker84@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()