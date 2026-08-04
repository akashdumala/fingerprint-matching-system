import streamlit as st
import tempfile

from matcher.matcher_engine import match_images

st.set_page_config(
    page_title="Fingerprint Matching System",
    page_icon="🔍",
    layout="centered"
)

st.title("Fingerprint Matching System")

image1 = st.file_uploader("Upload Fingerprint 1", type=["tif"])
image2 = st.file_uploader("Upload Fingerprint 2", type=["tif"])

if image1 and image2:

    st.success("Files uploaded successfully!")

    temp1 = tempfile.NamedTemporaryFile(delete=False, suffix=".tif")
    temp1.write(image1.read())
    temp1.close()

    temp2 = tempfile.NamedTemporaryFile(delete=False, suffix=".tif")
    temp2.write(image2.read())
    temp2.close()

    st.write("Calling match_images...")

    score = match_images(temp1.name, temp2.name)

    st.success("match_images executed successfully!")

    st.write("Similarity Score:", score)

   