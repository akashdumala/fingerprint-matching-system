import streamlit as st

st.set_page_config(
    page_title="Fingerprint Matching System",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 Fingerprint Matching System")

st.success("🎉 Streamlit deployment is working successfully!")

st.write("If you can see this page, the problem is NOT Streamlit Cloud.")
st.write("The issue is inside one of the fingerprint matching modules.")

st.markdown("---")

st.subheader("System Status")

st.write("✅ Streamlit Loaded")
st.write("✅ Python Working")
st.write("✅ Deployment Successful")

st.balloons()