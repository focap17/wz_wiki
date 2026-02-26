import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="World Zero Wiki", layout="wide", page_icon="⚔️")

# Inicializa o estado da página e da skill selecionada para evitar erros de navegação
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Home'
if 'skill_ativa' not in st.session_state:
    st.session_state.skill_ativa = "Sword Slash (LMB)"


def mudar_pagina(nome):
    st.session_state.pagina = nome


# --- 2. ESTILIZAÇÃO CSS (DESIGN MODERNO + ELEMENTOS DO JOGO) ---
st.markdown("""
<style>
    /* Fundo gradiente para profundidade */
    .stApp { background: radial-gradient(circle, #1a1f25 0%, #0d1117 100%); }
    
    .neon-title {
        font-size: 50px; font-weight: 900; color: #00ffcc; text-align: center;
        text-transform: uppercase; letter-spacing: 5px;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 0;
    }

    /* Estilos da Ficha Técnica da Classe */
    .weapon-tag { color: #00ffcc; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; }
    .class-name { font-size: 60px; font-weight: 800; color: #fff; margin-top: -10px; margin-bottom: 10px; }
    .lore-box { 
        font-style: italic; color: #ccc; font-size: 16px; line-height: 1.6; 
        border-left: 4px solid #00ffcc; padding-left: 20px; margin: 20px 0;
    }

    /* Barra de Vida baseada na imagem enviada */
    .health-label { color: #888; font-weight: bold; margin-bottom: 8px; display: block; font-size: 12px; }
    .health-grid { display: flex; gap: 8px; margin-bottom: 25px; }
    .h-block { width: 50px; height: 14px; border-radius: 3px; border: 1px solid #000; }
    .h-on { background: #00ff44; box-shadow: 0 0 10px rgba(0, 255, 68, 0.4); }
    .h-off { background: #333; }

    /* Caixa de Descrição da Habilidade */
    .skill-desc-box {
        background: rgba(0, 0, 0, 0.3);
        border: 1px solid #333;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        border-left: 5px solid #00ffcc;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. CABEÇALHO ---
st.markdown('<p class="neon-title">WORLD ZERO</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#666; letter-spacing:3px; margin-bottom:30px;">DATABASE & WIKI</p>', unsafe_allow_html=True)

# --- 4. MENU DE NAVEGAÇÃO ---
if st.session_state.pagina == 'Home':
    st.write("")
    cols = st.columns(4)
    menu = [("🛡️", "Builds"), ("⚔️", "Classes"),
            ("🐾", "Pets"), ("🗺️", "Mundos")]

    for i, (icon, nome) in enumerate(menu):
        with cols[i]:
            if st.button(f"{icon} {nome}", use_container_width=True):
                mudar_pagina(nome)
                st.rerun()

# --- 5. PÁGINA DE CLASSES (SUGESTÃO B - CORRIGIDA) ---
elif st.session_state.pagina == 'Classes':
    if st.button("⬅️ Voltar ao Menu"):
        mudar_pagina('Home')
        st.rerun()

    st.divider()

    # Dados do Swordmaster baseados na imagem e informações do jogo
    skills_sword = {
        "Sword Slash (LMB)": {"cd": "0s", "desc": "Your primary attack! Slash with fury to keep the pressure on.", "icon": "⚔️"},
        "Leaping Slash": {"cd": "6s", "desc": "Jump towards enemies and strike from above with a powerful blow.", "icon": "🦘"},
        "Blade Dance": {"cd": "12s", "desc": "Execute a whirlwind of strikes hitting all surrounding enemies.", "icon": "🌪️"},
        "Dash": {"cd": "4s", "desc": "Quickly reposition yourself to dodge attacks or close gaps.", "icon": "💨"}
    }

    col_info, col_char = st.columns([1.2, 1])

    with col_info:
        st.markdown(
            '<span class="weapon-tag">Weapon Type: Longsword</span>', unsafe_allow_html=True)
        st.markdown('<h1 class="class-name">Swordmaster</h1>',
                    unsafe_allow_html=True)

        # Sistema de Vida (4 de 5 blocos conforme a imagem)
        st.markdown(
            '<span class="health-label">HEALTH / RESISTANCE</span>', unsafe_allow_html=True)
        st.markdown("""
            <div class="health-grid">
                <div class="h-block h-on"></div>
                <div class="h-block h-on"></div>
                <div class="h-block h-on"></div>
                <div class="h-block h-on"></div>
                <div class="h-block h-off"></div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="lore-box">
                Born to wield the sword, the Swordmaster strikes their foes at the heart! 
                Slash with fury and focus to reign supreme!
            </div>
        """, unsafe_allow_html=True)

        # Seletor de Habilidades
        st.write("### ⚡ Abilities")
        c_icons = st.columns(len(skills_sword))
        for i, (nome_skill, info) in enumerate(skills_sword.items()):
            with c_icons[i]:
                # Cada botão funciona como um ícone clicável
                if st.button(info['icon'], key=f"btn_{nome_skill}", help=nome_skill):
                    st.session_state.skill_ativa = nome_skill

        # Caixa de Detalhes Dinâmica (Atualiza conforme o clique nos botões acima)
        skill_atual = skills_sword[st.session_state.skill_ativa]
        st.markdown(f"""
            <div class="skill-desc-box">
                <h3 style='margin:0; color:#00ffcc;'>{st.session_state.skill_ativa}</h3>
                <small style='color:#888;'>COOLDOWN: {skill_atual['cd']}</small>
                <p style='margin-top:15px; font-size:16px; color:#eee;'>{skill_atual['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

    with col_char:
        # Imagem do personagem (Pode substituir pelo link da imagem original cortada)
        st.image("https://i.imgur.com/3Z6O3Z8.png", use_container_width=True)
        st.write("")
        if st.button("EQUIP CLASS", type="primary", use_container_width=True):
            st.balloons()

# --- 6. PÁGINAS EM DESENVOLVIMENTO ---
else:
    if st.button("⬅️ Voltar"):
        mudar_pagina('Home')
        st.rerun()
    st.warning(
        f"A página de {st.session_state.pagina} ainda está a ser forjada pelos Ferreiros.")
