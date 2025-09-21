import os
import json
from typing import Optional

import streamlit as st
import requests
from utils.data import get_streams_data

API_URL = os.getenv("API_URL")


def check_api_health(base_url: str) -> Optional[dict]:
    try:
        resp = requests.get(f"{base_url.rstrip('/')}/health", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


st.title("🧭 Streams")

data = get_streams_data(API_URL)

summary_tab, explorer_tab = st.tabs(["Summary", "Explorer"])

with summary_tab:
    st.write(
        "Use this space to summarize streams (Science/Commerce/Arts), data coverage, and guidance methodology."
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Science", "Popular", "+")
    with col2:
        st.metric("Commerce", "Growing", "+")
    with col3:
        st.metric("Arts", "Varied", "+")

    st.markdown("### Data snapshot")
    st.dataframe(data, use_container_width=True)

with explorer_tab:
    options = [row.get("name", row.get("id")) for row in data] if data else ["Science", "Commerce", "Arts"]
    choice = st.selectbox("Choose a stream", options, index=0)
    st.text_input("Filter by aptitude / interests")
    st.button("Generate guidance")

if API_URL:
    status = check_api_health(API_URL)
    if status and not status.get("error") and status.get("ok") is True:
        st.caption("API: healthy")
    else:
        st.caption(f"API issue: {json.dumps(status)}")
