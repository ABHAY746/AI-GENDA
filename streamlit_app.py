import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key="AIzaSyBKb-aCZl6u1vife_bo4tCanXKG7bSm5cg")
model = genai.GenerativeModel('gemini-1.5-flash') 
def get_gemini_response(input_text,image_data,prompt):
    response= model.generate_content([input_text,image_data[0],prompt])
    return response.text
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            { 
             "mime_type": uploaded_file.type,
             "data":bytes_data
            }
        ]
        return image_parts
    else:
      raise FileNotFoundError("No file is uploaded")
st.set_page_config(page_title="WIE's invoice generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Abhay")
st.sidebar.write("Powered by google gemini")
st.header("RoboBill")
st.subheader("Made by Abhay")
st.subheader("Manage your expenses with with RoboBill")
input = st.text_input("what do you want me to do? ",key="input")
uploaded_file = st.file_uploader("choose an image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image =Image.open(uploaded_file)
    st.image(image,caption="uploaded Image", use_column_width=True)
submit=st.button("Let's GO!!")
input_prompt = """
you are an expert in understanding invoices. 
We will upload a image as invoices 
and you will have to answer any questions based on the uploaded invoice image
Make sure to greet the user first and then provide the information as suited.
Make sure to keep the font uniform and give the items list in a point-wise format.
At the end, make sure to repeat the name of our app "RoboBill 🦾" and ask the user to use it again."""
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know:")
    st.write(response)
 
