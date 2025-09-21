import os
import json
from typing import Optional

import streamlit as st
import requests
from utils.data import get_skills_data

API_URL = os.getenv("API_URL")


def check_api_health(base_url: str) -> Optional[dict]:
    try:
        resp = requests.get(f"{base_url.rstrip('/')}/health", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


st.title("🧠 Skills")

reco_tab, trends_tab = st.tabs(["Recommender", "Trends"])

with reco_tab:
    role = st.text_input("Target role / field", value="Software Engineer")
    st.slider("Experience (years)", 0, 20, 0)
    data = get_skills_data(API_URL, role=role)
    st.dataframe(data, use_container_width=True)

with trends_tab:
    st.write("Snapshot of skills data:")
    data = get_skills_data(API_URL)
    st.dataframe(data, use_container_width=True)

if API_URL:
    status = check_api_health(API_URL)
    if status and not status.get("error") and status.get("ok") is True:
        st.caption("API: healthy")
    else:
        st.caption(f"API issue: {json.dumps(status)}")
