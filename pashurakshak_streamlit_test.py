import streamlit as st

st.set_page_config(
    page_title="PashuRakshak AI",
    page_icon="🐄",
    layout="wide"
)

st.title("PashuRakshak AI")

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #15803d, #0f766e);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
    ">
        <h1>PashuRakshak AI</h1>
        <p>AI-powered livestock health screening</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("If you can see the green card above normally, HTML rendering is working.")
