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

if image1 is not None and image2 is not None:

    temp1 = tempfile.NamedTemporaryFile(delete=False, suffix=".tif")
    temp1.write(image1.read())
    temp1.close()

    temp2 = tempfile.NamedTemporaryFile(delete=False, suffix=".tif")
    temp2.write(image2.read())
    temp2.close()

    try:
        score = match_images(temp1.name, temp2.name)

        st.success("Matching Completed")

        st.subheader("Similarity Score")
        st.write(f"### {score:.4f}")

        if score >= 0.03:
            st.success("✅ Fingerprints Match")
        else:
            st.error("❌ Fingerprints Do Not Match")

    except Exception as e:
        st.error(f"Error: {e}")

    finally:
        if os.path.exists(temp1.name):
            os.remove(temp1.name)

        if os.path.exists(temp2.name):
            os.remove(temp2.name)