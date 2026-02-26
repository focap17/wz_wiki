# styles.py
import streamlit as st


def apply_styles():
    st.markdown("""
    <style>
        /* Esconder menu lateral e poluição visual */
        [data-testid="stSidebar"], section[data-testid="stSidebarNav"] {display: none;}
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Seu Design Neon */
        .stApp { background: radial-gradient(circle, #1a1f25 0%, #0d1117 100%); }
        .neon-title { font-size: 50px; font-weight: 900; color: #00ffcc; text-align: center; text-transform: uppercase; letter-spacing: 5px; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 30px; }
        .stat-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 255, 204, 0.1); padding: 15px; border-radius: 10px; text-align: center; }
        .stat-label { color: #888; font-size: 11px; text-transform: uppercase; font-weight: bold; }
        .stat-value { color: #fff; font-size: 16px; font-weight: bold; }
        .class-name { font-size: 55px; font-weight: 800; color: #fff; margin: 0; }
        .skill-desc-box { background: rgba(0,0,0,0.4); border: 1px solid #333; padding: 25px; border-radius: 12px; border-left: 5px solid #00ffcc; }
        .build-card-container { background-color: #0b4c8c; border-radius: 12px; padding: 18px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.5); margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.1); }
        .header-row { display: flex; gap: 12px; align-items: center; margin-bottom: 12px; }
    </style>
    """, unsafe_allow_html=True)
