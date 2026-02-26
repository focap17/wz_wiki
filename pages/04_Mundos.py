import streamlit as st
from styles import apply_styles

st.set_page_config(page_title="World Zero Wiki",
                   layout="wide", initial_sidebar_state="collapsed")
apply_styles()

# --- BOTÃO DE VOLTAR ---
if st.button("⬅️ VOLTAR AO MENU PRINCIPAL"):
    st.switch_page("home.py")

st.warning("Página em desenvolvimento...")
