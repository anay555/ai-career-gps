import os
import json
from typing import Optional

import streamlit as st
import requests

st.set_page_config(page_title="AI Career GPS", layout="wide")

TAGLINE = "Data-Driven Career GPS: From Stream to Startup"
API_URL = os.getenv("API_URL")  # Optional: e.g. https://your-api.example.com


def check_api_health(base_url: str) -> Optional[dict]:
    try:
        resp = requests.get(f"{base_url.rstrip('/')}/health", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


st.title("AI Career GPS")
st.caption(TAGLINE)

with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Go to",
        [
            "Overview",
            "Streams",
            "Colleges",
            "Skills",
            "About",
        ],
        index=0,
    )

    st.divider()
    st.subheader("API Status")
    if API_URL:
        status = check_api_health(API_URL)
        if status and not status.get("error") and status.get("ok") is True:
            st.success("API healthy")
        else:
            st.error(f"API issue: {json.dumps(status)}")
        st.code(f"API_URL={API_URL}")
    else:
        st.info(
            "Set an API_URL environment variable in Streamlit Cloud Secrets to enable live API checks."
        )

if page == "Overview":
    st.subheader("Problem")
    st.write(
        "Students struggle with stream, college, and career choices due to vague guidance,"
        " outdated data, and lack of entrepreneurship insights."
    )

    st.subheader("Solution")
    st.write(
        "An AI-powered career pathway platform guiding students from stream selection → college"
        " choice → skills → jobs/startups, using real data & market insights."
    )

    st.subheader("Key Features")
    st.markdown(
        "- Stream Guidance (Class 10): Aptitude + interest → Science/Commerce/Arts with salary, jobs, business options.\n"
        "- Education vs Industry Gap: Live analytics on graduate supply vs job demand.\n"
        "- College Engine: Compare real packages, research, entrepreneurship ecosystem.\n"
        "- AI Skill Recommender: Future-proof skills + personalized roadmaps.\n"
        "- Degree + Entrepreneurship Path: Degrees linked to startup opportunities + case studies."
    )

    st.subheader("Roadmap (high level)")
    st.markdown(
        "- v0: Data model, API endpoints for guidance, initial analytics stubs\n"
        "- v1: Next.js UI with stream guidance flow and dashboards\n"
        "- v2: Integrations (job market data), AI skill recommender\n"
        "- v3: College engine, entrepreneurship pathways, advanced visualizations"
    )

elif page == "Streams":
    st.subheader("Streams Explorer (stub)")
    st.info("This is a placeholder. Connect to data/ or an API to populate.")

elif page == "Colleges":
    st.subheader("Colleges (stub)")
    st.info("This is a placeholder. Connect to data/ or an API to populate.")

elif page == "Skills":
    st.subheader("Skills & Recommendations (stub)")
    st.info("This is a placeholder. Connect to data/ or an API to populate.")

elif page == "About":
    st.subheader("About this app")
    st.write("This Streamlit app is a lightweight UI shell to host on Streamlit Cloud.")
    st.markdown(
        "- Optional: set API_URL secret to call a hosted API for live data.\n"
        "- Local data guidance: see data/README.md"
    )
