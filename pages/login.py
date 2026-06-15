import streamlit as st
import requests

server_url = "http://127.0.0.1:8000"

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if not email or not password:
        st.error("Fill all fields")
        st.stop()

    payload = {
        "email": email,
        "password": password
    }

    res = requests.post(f"{server_url}/login", json=payload)
    data = res.json()

    if data.get("message") == "Login successful":

        st.session_state["logged_in"] = True
        st.session_state["user"] = data["data"]

        st.success("Login Successful")

        st.switch_page("pages/founder_dashboard.py")

    else:
        st.error("Invalid credentials")