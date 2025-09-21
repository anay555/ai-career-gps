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


st.title("🏛️ Colleges")

compare_tab, insights_tab = st.tabs(["Compare (stub)", "Insights (stub)"])

with compare_tab:
    st.info("Placeholder: compare colleges by package, research, entrepreneurship support.")
    st.multiselect("Colleges to compare", ["College A", "College B", "College C"], default=["College A"])
    st.selectbox("Metric", ["Package", "Research", "Entrepreneurship"], index=0)
    st.button("Compare")

with insights_tab:
    st.info("Placeholder: show analytics on education vs industry gap and ecosystems.")

if API_URL:
    status = check_api_health(API_URL)
    if status and not status.get("error") and status.get("ok") is True:
        st.caption("API: healthy")
    else:
        st.caption(f"API issue: {json.dumps(status)}")
