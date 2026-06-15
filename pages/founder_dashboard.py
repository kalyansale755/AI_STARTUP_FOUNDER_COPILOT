import streamlit as st
import requests
import json

st.set_page_config(page_title="Founder Dashboard", page_icon="🚀", layout="wide")

if not st.session_state.get("logged_in"):
    st.switch_page("pages/login.py")

server_url = "http://127.0.0.1:8000"

st.title("🚀 Founder Dashboard")

startup_idea = st.text_area("Enter Startup Idea")

if st.button("Analyze Startup Idea"):

    if not startup_idea:
        st.error("Please enter startup idea")
        st.stop()

    st.session_state["startup_idea"] = startup_idea

    try:
        res = requests.post(
            f"{server_url}/analyze",
            json={"startup_idea": startup_idea}
        )

        data = res.json()
        st.session_state["analysis"] = data.get("analysis", "")

    except Exception as e:
        st.error(f"Error: {e}")

if st.session_state.get("analysis"):

    st.divider()
    st.subheader("AI Analysis Result")

    try:
        st.json(json.loads(st.session_state["analysis"]))
    except:
        st.write(st.session_state["analysis"])

st.divider()

st.subheader("Dashboards")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Market Dashboard"):
        st.switch_page("pages/market_dashboard.py")

with col2:
    if st.button("Finance Dashboard"):
        st.switch_page("pages/finance_dashboard.py")

with col3:
    if st.button("Reports Dashboard"):
        st.switch_page("pages/reports.py")

st.divider()

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("pages/login.py")