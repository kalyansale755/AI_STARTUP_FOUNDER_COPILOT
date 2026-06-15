import streamlit as st
import requests

server_url = "http://127.0.0.1:8000"

st.title("📝 Register")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):

    if not name or not email or not password:
        st.error("Fill all fields")
        st.stop()

    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    res = requests.post(f"{server_url}/register", json=payload)

    if res.status_code == 200:
        st.success("Registered Successfully")
        st.info("Now go to Login page")
    else:
        st.error("Registration Failed")