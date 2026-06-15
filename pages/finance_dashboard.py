import streamlit as st
import requests

st.set_page_config(page_title="Finance Dashboard", page_icon="💰", layout="wide")

if not st.session_state.get("logged_in"):
    st.switch_page("pages/login.py")

server_url = "http://127.0.0.1:8000"

st.title("💰 Finance Analysis Dashboard")

idea = st.session_state.get("startup_idea")

if not idea:
    st.warning("No startup idea found")
    st.stop()

st.info(f"Startup Idea: {idea}")

if st.button("Generate Finance Analysis"):

    res = requests.post(
        f"{server_url}/analyze",
        json={"startup_idea": idea}
    )

    data = res.json()
    analysis = data["analysis"]

    st.subheader("🤖 AI Financial Analysis")
    st.write(analysis)

    st.divider()

    st.subheader("📊 Finance Insights")

    st.markdown("""
    - Revenue potential discussed in AI output
    - Cost estimation included in analysis
    - Profit opportunities identified
    - Investment feasibility evaluated
    """)

st.divider()

if st.button("⬅ Back to Founder Dashboard"):
    st.switch_page("pages/founder_dashboard.py")