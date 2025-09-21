import streamlit as st

st.title("ℹ️ About")

st.markdown(
    """
    This Streamlit app is a modern, multipage shell for AI Career GPS.

    - Navigate via the left pages menu.  
    - Optional: set `API_URL` as a secret to connect a hosted API.  
    - For data layout guidance: see `data/README.md`.
    """
)

st.subheader("Design notes")
st.markdown(
    """
    - Uses a hero section and metrics on the landing page.  
    - Pages use tabs for sub-navigation and a consistent dark theme.  
    - Minimal CSS for a more modern feel (rounded cards, subtle gradients).
    """
)
