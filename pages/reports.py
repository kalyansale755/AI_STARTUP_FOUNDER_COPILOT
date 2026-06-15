import streamlit as st
import requests

st.set_page_config(page_title="AI Reports Dashboard", page_icon="📊", layout="wide")

if not st.session_state.get("logged_in"):
    st.switch_page("pages/login.py")

server_url = "http://127.0.0.1:8000"

st.title("📊 AI Reports Dashboard")

try:
    res = requests.get(f"{server_url}/reports")

    if res.status_code == 200:
        reports = res.json()
    else:
        reports = []

except:
    reports = []

st.metric("Total Reports", len(reports))

st.divider()

if len(reports) == 0:
    st.warning("No reports found. Generate analysis from Founder Dashboard.")
else:
    market = []
    finance = []
    other = []

    for r in reports:
        rtype = r.get("report_type", "").lower()

        if "market" in rtype:
            market.append(r)
        elif "finance" in rtype:
            finance.append(r)
        else:
            other.append(r)

    st.subheader("📈 Market Analysis Reports")
    if market:
        for r in market:
            st.write(r.get("report_content", ""))
            st.divider()
    else:
        st.info("No market reports")

    st.subheader("💰 Financial Analysis Reports")
    if finance:
        for r in finance:
            st.write(r.get("report_content", ""))
            st.divider()
    else:
        st.info("No financial reports")

    st.subheader("🎯 Other Reports")
    if other:
        for r in other:
            st.write(r.get("report_content", ""))
            st.divider()

st.divider()

if st.button("⬅ Back to Founder Dashboard"):
    st.switch_page("pages/founder_dashboard.py")