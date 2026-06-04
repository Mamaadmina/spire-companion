from textwrap import dedent

import streamlit as st


def render_html(markup):
    html = "\n".join(
        line.lstrip() for line in dedent(markup).strip().splitlines()
    )

    if hasattr(st, "html"):
        st.html(html)
    else:
        st.markdown(html, unsafe_allow_html=True)
