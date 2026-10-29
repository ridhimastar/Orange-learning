import streamlit as st
st.title("Interactive streamlit app")
name=st.text_input("Enter ur name:")
if st.button("Submit"):
  st.write(f"Hello,{name}! Welcome to streamlit.")
