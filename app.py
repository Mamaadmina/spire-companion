import streamlit as st

from home import show_home


st.set_page_config(
    page_title="SPIRE",
    page_icon=":crystal_ball:",
    layout="wide",
)

show_home()
