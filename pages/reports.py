import streamlit as st
import requests

st.set_page_config(
    page_title="AI Reports Dashboard",
    page_icon="📊",
    layout="wide"
)

if not st.session_state.get("logged_in"):
    st.switch_page("pages/login.py")

API_URL = "http://127.0.0.1:8000"

st.title("📊 AI Reports Dashboard")

if st.button("🔄 Refresh Reports"):
    st.rerun()

try:
    response = requests.get(f"{API_URL}/reports", timeout=10)

    if response.status_code == 200:
        reports = response.json()
    else:
        reports = []
        st.error("Unable to fetch reports from server.")

except Exception as e:
    reports = []
    st.error(f"Connection Error: {e}")

st.metric("Total Reports", len(reports))

st.divider()

if not reports:
    st.info("No reports available. Generate an analysis from Founder Dashboard.")
else:
    for index, report in enumerate(reports, start=1):
        report_type = report.get("report_type", "AI Report")
        report_content = report.get("report_content", "")

        with st.expander(f"📄 Report {index} - {report_type}"):
            st.write(report_content)

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Back to Founder Dashboard"):
        st.switch_page("pages/founder_dashboard.py")

with col2:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("pages/login.py")