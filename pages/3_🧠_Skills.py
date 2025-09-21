import os
import json
from typing import Optional

import streamlit as st
import requests

API_URL = os.getenv("API_URL")


def check_api_health(base_url: str) -> Optional[dict]:
    try:
        resp = requests.get(f"{base_url.rstrip('/')}/health", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


st.title("🧠 Skills")

reco_tab, trends_tab = st.tabs(["Recommender (stub)", "Trends (stub)"])

with reco_tab:
    st.info("Placeholder: personalized skill recommendations and roadmaps.")
    st.text_input("Target role / field")
    st.slider("Experience (years)", 0, 20, 0)
    st.button("Get recommendations")

with trends_tab:
    st.info("Placeholder: show skill demand and salary trends.")

if API_URL:
    status = check_api_health(API_URL)
    if status and not status.get("error") and status.get("ok") is True:
        st.caption("API: healthy")
    else:
        st.caption(f"API issue: {json.dumps(status)}")
