import streamlit as st

def set_page_style():
    """Applies custom design styles to the Streamlit app."""
    st.markdown("""
        <style>
        body {
            background-color: #f0f8ff;
            font-family: 'Arial';
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stTextInput input {
            border: 2px solid #4CAF50;
        }
        </style>
        """, unsafe_allow_html=True)
