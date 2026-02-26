# styles.py
import streamlit as st


def apply_styles():
    st.markdown("""
    <style>
        /* 1. Limpeza de Interface */
        [data-testid="stSidebar"], section[data-testid="stSidebarNav"] {display: none;}
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* 2. Fundo e Título */
        .stApp { 
            background: radial-gradient(circle, #1a1f25 0%, #0d1117 100%); 
        }
        .neon-title { 
            font-size: 60px; 
            font-weight: 900; 
            color: #00ffcc; 
            text-align: center; 
            text-transform: uppercase; 
            letter-spacing: 8px; 
            text-shadow: 0 0 20px rgba(0, 255, 204, 0.6); 
            margin-bottom: 5px; 
        }
        .subtitle {
            color: #888;
            text-align: center;
            font-size: 18px;
            margin-bottom: 50px;
            letter-spacing: 2px;
        }

        /* 3. BOTÕES GAMER CUSTOMIZADOS */
        div.stButton > button {
            background: rgba(0, 255, 204, 0.03) !important;
            border: 2px solid #00ffcc !important;
            color: #00ffcc !important;
            border-radius: 15px !important;
            height: 120px !important; /* Mais altos */
            font-size: 22px !important;
            font-weight: bold !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            box-shadow: inset 0 0 10px rgba(0, 255, 204, 0.1) !important;
        }

        /* Efeito ao passar o mouse */
        div.stButton > button:hover {
            background: #00ffcc !important;
            color: #0d1117 !important;
            box-shadow: 0 0 30px rgba(0, 255, 204, 0.8) !important;
            transform: translateY(-8px) scale(1.02) !important;
        }

        /* Ajustes de Layout das outras páginas */
        .stat-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 255, 204, 0.1); padding: 15px; border-radius: 10px; text-align: center; }
        .skill-desc-box { background: rgba(0,0,0,0.4); border: 1px solid #333; padding: 25px; border-radius: 12px; border-left: 5px solid #00ffcc; }
        .build-card-container { background-color: #0b4c8c; border-radius: 12px; padding: 18px; color: white; margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.1); }
    </style>
    
    """, unsafe_allow_html=True)
