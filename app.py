import os
import tempfile

import streamlit as st

from matcher.matcher_engine import match_images


st.set_page_config(
    page_title="Fingerprint Matching System",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 Fingerprint Matching System")

st.write("Upload two fingerprint images to compare them.")

image1 = st.file_uploader(
    "Upload Fingerprint 1",
    type=["tif", "png", "jpg", "jpeg"]
)

image2 = st.file_uploader(
    "Upload Fingerprint 2",
    type=["tif", "png", "jpg", "jpeg"]
)

if image1 and image2:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".tif") as temp1:
        temp1.write(image1.read())
        path1 = temp1.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".tif") as temp2:
        temp2.write(image2.read())
        path2 = temp2.name

    score = match_images(path1, path2)

    st.success("Matching Completed")

    st.metric(
        "Similarity Score",
        f"{score:.4f}"
    )

    os.remove(path1)
    os.remove(path2)