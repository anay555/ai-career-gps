import os
import json
from typing import Optional

import streamlit as st
import requests
from utils.data import get_colleges_data

API_URL = os.getenv("API_URL")


def check_api_health(base_url: str) -> Optional[dict]:
    try:
        resp = requests.get(f"{base_url.rstrip('/')}/health", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


st.title("🏛️ Colleges")

colleges = get_colleges_data(API_URL)

compare_tab, insights_tab = st.tabs(["Compare", "Insights"])

with compare_tab:
    st.write("Compare colleges by package, research, and entrepreneurship support.")
    names = [c.get("name", c.get("id")) for c in colleges] if colleges else []
    selected = st.multiselect("Colleges to compare", names, default=names[:1])
    metric = st.selectbox("Metric", ["package_median_lpa", "research_index", "entrepreneurship_support"], index=0)

    if selected and colleges:
        rows = [c for c in colleges if c.get("name") in selected]
        st.dataframe(rows, use_container_width=True)

with insights_tab:
    st.write("Snapshot of available college records:")
    st.dataframe(colleges, use_container_width=True)

if API_URL:
    status = check_api_health(API_URL)
    if status and not status.get("error") and status.get("ok") is True:
        st.caption("API: healthy")
    else:
        st.caption(f"API issue: {json.dumps(status)}")
