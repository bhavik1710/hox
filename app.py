from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#model=genai.GenerativeModel("gemini-flash-1.5")

model=genai.GenerativeModel("gemini-1.5-pro")

def my_output(query):
    response=model.generate_content(query)
    return response.text

st.set_page_config(page_title="SOLUTION_WITH_BHAVIK")
st.header("SOLUTION_WITH_BHAVIK")
input=st.text_input("input",key="input")
submit=st.button("find your answer")

if submit:
    response=my_output(input)
    st.subheader("The Response is=")
    st.write(response)