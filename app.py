import streamlit as st

st.title("AI STARTUP FOUNDER COPILOT")

if st.button("Register"):
    st.switch_page("pages/register.py")

if st.button("Login"):
    st.switch_page("pages/login.py")


