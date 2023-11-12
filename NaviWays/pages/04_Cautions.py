import streamlit as st
from constants import *

background_css = """
    <style>
        body {
            background-color: #e5e5f7;
            opacity: 0.95;
            background-image: repeating-radial-gradient(circle at 0 0, transparent 0, #e5e5f7 50px), repeating-linear-gradient(#444cf755, #444cf7);
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
    </style>
"""

st.markdown(background_css, unsafe_allow_html=True)