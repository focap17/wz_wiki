import streamlit as st
from styles import apply_styles

st.set_page_config(page_title="World Zero Wiki", layout="wide", page_icon="⚔️")
apply_styles()

st.markdown('<p class="neon-title">WORLD ZERO DATABASE</p>',
            unsafe_allow_html=True)

cols = st.columns(4)
menu = [("🛡️ Builds", "pages/01_Builds.py"),
        ("⚔️ Classes", "pages/02_Classes.py"),
        ("🐾 Pets", "pages/03_Pets.py"),
        ("🗺️ Mundos", "pages/04_Mundos.py")]

for i, (label, path) in enumerate(menu):
    with cols[i]:
        if st.button(label, use_container_width=True):
            st.switch_page(path)
