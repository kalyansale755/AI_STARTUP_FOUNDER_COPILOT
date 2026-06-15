import streamlit as st
import requests
import json

st.set_page_config(page_title="Market Dashboard", page_icon="📈", layout="wide")

if not st.session_state.get("logged_in"):
    st.switch_page("pages/login.py")

server_url = "http://127.0.0.1:8000"

st.title("📈 Market Analysis Dashboard")

idea = st.session_state.get("startup_idea")

if not idea:
    st.warning("No startup idea found")
    st.stop()

st.info(f"Startup Idea: {idea}")

if st.button("Generate Market Analysis"):

    try:
        res = requests.post(
            f"{server_url}/analyze",
            json={"startup_idea": idea}
        )

        data = res.json()

        raw = data.get("analysis", "")

        st.success("Analysis Generated")

        st.subheader("📊 Key Metrics")

        structured = None

        try:
            structured = json.loads(raw)
        except:
            structured = None

        if structured:

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Market Size", structured.get("market_size", "N/A"))

            with col2:
                st.metric("Competitors", structured.get("competitors", "N/A"))

            with col3:
                st.metric("Growth Rate", structured.get("growth_rate", "N/A"))

        else:

            st.warning("Numbers not available, showing fallback")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Market Size", "N/A")

            with col2:
                st.metric("Competitors", "N/A")

            with col3:
                st.metric("Growth Rate", "N/A")

        st.divider()

        st.subheader("📦 Full JSON Output")

        try:
            st.json(json.loads(raw))
        except:
            st.write(raw)

    except Exception as e:
        st.error(f"Error: {e}")

st.divider()

if st.button("⬅ Back to Founder Dashboard"):
    st.switch_page("pages/founder_dashboard.py")