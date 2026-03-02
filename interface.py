import streamlit as st


def aplicar_estilo():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Rajdhani:wght@600;700&display=swap');

    /* 1. RESET DE PADDING (A BASE DA SIMETRIA) */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
        padding-left: 5rem !important;
        padding-right: 5rem !important;
    }
    
    /* No interface.py */
.content-card {
    background: rgba(255, 255, 255, 0.03);
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #f1c40f;
    margin-bottom: 20px !important; /* Isso garante o espaço igual entre eles */
}

    /* 2. REMOVE SIDEBAR */
    section[data-testid="stSidebar"] { display: none !important; }

    /* 3. FUNDO E FONTE GLOBAL */
    .main { 
        background: radial-gradient(circle at top, #151c2b 0%, #05070a 80%) !important;
        color: #e0e0e0 !important;
        font-family: 'Rajdhani', sans-serif !important;
    }

    /* 4. HEADER (TÍTULO) TRAVADO */
    .header-wiki {
        font-family: 'Rajdhani', cursive !important;
        font-size: 45px !important;
        text-align: center !important;
        letter-spacing: 3px !important;
        background: linear-gradient(90deg, #f1c40f, #ff9800, #ffffff, #f1c40f) !important;
        background-size: 400% 400% !important;
        color: transparent !important;
        -webkit-background-clip: text !important;
        animation: shine 4s ease infinite !important;
        margin-bottom: 0px !important;
        line-height: 1.1 !important;
    }
    @keyframes shine { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }

    /* 5. CARDS DE ESTATÍSTICAS */
    .nav-stats {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(241, 196, 15, 0.15) !important;
        border-radius: 6px !important;
        text-align: center !important;
        height: 70px !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-bottom: 10px !important;
    }
    .stat-value { color: #f1c40f !important; font-weight: bold !important; font-size: 18px !important; line-height: 1 !important; }
    .stat-label { color: #aaa !important; font-size: 9px !important; text-transform: uppercase !important; margin-top: 4px !important; }

    /* 6. BOTÕES DE NAVEGAÇÃO */
    div.stButton > button {
        width: 100% !important;
        background-color: #0c1220 !important;
        color: #f1c40f !important;
        border: 1.2px solid #4a3f10 !important;
        border-radius: 4px !important;
        height: 42px !important;
        font-weight: bold !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
    }
    div.stButton > button:hover {
        border-color: #f1c40f !important;
        box-shadow: 0 0 10px rgba(241, 196, 15, 0.2) !important;
    }

    /* 7. ESTILO DE CARDS DE CONTEÚDO */
    .content-card {
        background: rgba(255, 255, 255, 0.02);
        border-left: 3px solid #f1c40f;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 15px;
    }

    /* 8. SEPARADOR TRACEJADO */
    .divisor-tracejado {
        border-top: 1px dashed #4a3f10;
        margin-top: 25px;
        margin-bottom: 25px;
        opacity: 0.6;
    }

    /* 9. NOVO ESTILO BALÃO DE TAG (FIXED) */
    .perk-tag {
        display: inline-block !important; /* Essencial para que o flex-wrap funcione */
        background: rgba(0, 255, 200, 0.08) !important;
        border: 1.5px solid #00FFC8 !important;
        color: #00FFC8 !important;
        padding: 6px 16px !important;
        border-radius: 30px !important;
        margin: 4px !important;
        font-size: 8px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 0 10px rgba(0, 255, 200, 0.15);
        white-space: nowrap !important; /* Impede que o texto quebre dentro da tag */
    }

    .perk-tag:hover {
        background: rgba(0, 255, 200, 0.2) !important;
        box-shadow: 0 0 18px rgba(0, 255, 200, 0.5) !important;
        transform: translateY(-2px);
    }

    /* 10. TÍTULOS DE SEÇÃO DE PERK (FIXED) */
    .perks-section-title {
        color: #aaa;
        font-size: 10px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 6px;
        margin-top: 15px; /* Espaço acima do título */
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* 11. CONTAINER DE EXIBIÇÃO DE PERKS (FLEXBOX) */
    .perks-display-area {
        display: flex !important;
        flex-wrap: wrap !important; /* Permite que as tags quebrem de linha se necessário */
        gap: 0px; /* O margin individual das tags cuida do espaço */
        align-items: flex-start;
        margin-top: -4px; /* Compensa o margin individual das tags */
    }
    </style>
    """, unsafe_allow_html=True)


def exibir_cabecalho(dados):
    st.markdown('<h1 class="header-wiki">WORLD//ZERO - COMUNIDADE BRASILEIRA</h1>',
                unsafe_allow_html=True)
    st.markdown(
        f'<div style="text-align:center; margin-top:-5px; margin-bottom: 25px;"><span style="color:#666; letter-spacing:2px; font-size:11px;">⚔️ ÚLTIMA ATUALIZAÇÃO: {dados["home"].get("ultima_atualizacao", "01/03/2026")}</span></div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    # REMOVEMOS O "st." daqui de baixo:
    with c1:
        nav_stats(dados, "builds", "🛡️ BUILDS")
    with c2:
        nav_stats(dados, "pets", "🐾 PETS")
    with c3:
        nav_stats(dados, "mundos", "🌍 MUNDOS", 10)
    with c4:
        nav_stats(dados, "classes", "⚔️ CLASSES", 22)

# Garanta que a função nav_stats não comece com "st." na definição dela


def nav_stats(dados, chave, label, valor_padrao=0):
    valor = len(dados.get(chave, [])) if valor_padrao == 0 else valor_padrao
    st.markdown(
        f'<div class="nav-stats"><span class="stat-value">{valor}</span><span class="stat-label">{label}</span></div>', unsafe_allow_html=True)


def nav_stats(dados, chave, label, valor_padrao=0):
    valor = len(dados.get(chave, [])) if valor_padrao == 0 else valor_padrao
    st.markdown(
        f'<div class="nav-stats"><span class="stat-value">{valor}</span><span class="stat-label">{label}</span></div>', unsafe_allow_html=True)


def exibir_nav(pagina_atual):
    st.write("")
    cols = st.columns(5, gap="small")
    btns = ["INÍCIO", "BUILDS", "TUTORIAIS", "DISCORD", "GUIA DE PREÇOS"]
    pags = {
        "INÍCIO": "app.py",
        "BUILDS": "pages/1_Builds.py",
        "TUTORIAIS": "pages/2_Tutoriais.py",
        "DISCORD": "pages/3_Discord.py",
        "GUIA DE PREÇOS": "pages/marketplace.py"
    }
    for col, nome in zip(cols, btns):
        with col:
            if st.button(nome, key=f"nav_{nome}", use_container_width=True):
                if nome == pagina_atual:
                    st.rerun()
                else:
                    st.switch_page(pags[nome])
    st.write("---")
