import streamlit as st

from matcher.matcher_engine import match_images

st.set_page_config(
    page_title="Fingerprint Matching System",
    page_icon="🔍",
    layout="centered"
)

st.title("Fingerprint Matching System")

st.success("Imports successful!")