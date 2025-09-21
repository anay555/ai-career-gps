import os
import json
from typing import Optional

import streamlit as st
import requests

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
FAVICON_PATH = os.path.join(ASSETS_DIR, "favicon.png")
PAGE_ICON = FAVICON_PATH if os.path.exists(FAVICON_PATH) else "🧭"

st.set_page_config(page_title="AI Career GPS", page_icon=PAGE_ICON, layout="wide")

TAGLINE = "Data-Driven Career GPS: From Stream to Startup"
API_URL = os.getenv("API_URL")  # Optional: e.g. https://your-api.example.com

# --- Minimal custom CSS for a modern look ---
st.markdown(
    """
    <style>
      .hero {
        padding: 2.25rem 2rem;
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(90,103,216,0.25), rgba(99,102,241,0.10));
        border: 1px solid rgba(99,102,241,0.35);
      }
      .hero h1 { margin: 0 0 0.5rem 0; font-size: 2.0rem; }
      .muted { color: #9CA3AF; }
      .card {
        background: rgba(17,24,39,0.6);
        border: 1px solid rgba(75,85,99,0.6);
        border-radius: 12px;
        padding: 1rem 1.25rem;
      }
    </style>
    """,
    unsafe_allow_html=True,
)


def check_api_health(base_url: str) -> Optional[dict]:
    try:
        resp = requests.get(f"{base_url.rstrip('/')}/health", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}

# --- Sidebar: API status and links ---
with st.sidebar:
    # Optional logo
    logo_path = os.path.join(ASSETS_DIR, "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, use_column_width=True)

    st.header("⚙️ System")
    if API_URL:
        status = check_api_health(API_URL)
        if status and not status.get("error") and status.get("ok") is True:
            st.success("API healthy")
        else:
            st.error(f"API issue: {json.dumps(status)}")
        st.caption(f"API_URL={API_URL}")
    else:
        st.info(
            "Set API_URL in Streamlit Cloud Secrets to enable live API checks."
        )

    st.divider()
    st.caption("AI Career GPS • v0 preview")

# --- Hero section ---
hero = st.container()
with hero:
    st.markdown(
        f"""
        <div class="hero">
          <h1>🧭 AI Career GPS</h1>
          <div class="muted">{TAGLINE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Quick metrics/cards ---
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    st.metric("Streams", "3", "+0")
with col2:
    st.metric("Colleges", "~1000+", "+")
with col3:
    st.metric("Skills", "200+", "+")
with col4:
    st.metric("Entrepreneurship", "Ideas", "∞")

st.divider()

# --- Tabs within the landing page ---
overview_tab, roadmap_tab, getting_started_tab = st.tabs([
    "Overview",
    "Roadmap",
    "Getting Started",
])

with overview_tab:
    left, right = st.columns([1.2, 1])
    with left:
        st.subheader("Problem")
        st.write(
            "Students struggle with stream, college, and career choices due to vague guidance, "
            "outdated data, and lack of entrepreneurship insights."
        )
        st.subheader("Solution")
        st.write(
            "An AI-powered career pathway platform guiding students from stream selection → college "
            "choice → skills → jobs/startups, using real data & market insights."
        )
        st.subheader("Key Features")
        st.markdown(
            "- Stream Guidance (Class 10): Aptitude + interest → Science/Commerce/Arts with salary, jobs, business options.\n"
            "- Education vs Industry Gap: Live analytics on graduate supply vs job demand.\n"
            "- College Engine: Compare real packages, research, entrepreneurship ecosystem.\n"
            "- AI Skill Recommender: Future-proof skills + personalized roadmaps.\n"
            "- Degree + Entrepreneurship Path: Degrees linked to startup opportunities + case studies."
        )
    with right:
        st.markdown("### Quick Links")
        st.markdown(
            "- Navigate pages via the left sidebar or the top 'pages' menu.\n"
            "- Check API status in the sidebar.\n"
            "- Data notes in data/README.md."
        )
        st.markdown("### Tips")
        st.info("Use the dedicated pages (left) for Streams, Colleges, Skills.")

with roadmap_tab:
    st.subheader("Roadmap (high level)")
    st.markdown(
        "- v0: Data model, API endpoints for guidance, initial analytics stubs\n"
        "- v1: Next.js UI with stream guidance flow and dashboards\n"
        "- v2: Integrations (job market data), AI skill recommender\n"
        "- v3: College engine, entrepreneurship pathways, advanced visualizations"
    )

with getting_started_tab:
    st.subheader("Local development")
    st.code(
        "python -m venv .venv\n.\\.venv\\Scripts\\Activate.ps1\npip install -r requirements.txt\nstreamlit run streamlit_app.py",
        language="bash",
    )
    st.subheader("Deploy (Streamlit Cloud)")
    st.markdown(
        "- Entry: streamlit_app.py\n"
        "- Secrets: .streamlit/secrets.template.toml → Cloud Secrets UI\n"
        "- Optional API_URL for live health"
    )
