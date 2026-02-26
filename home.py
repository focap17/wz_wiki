import streamlit as st
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="World Zero Wiki", layout="wide", page_icon="⚔️")

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Home'
if 'classe_selecionada' not in st.session_state:
    st.session_state.classe_selecionada = "Swordmaster"
if 'skill_ativa' not in st.session_state:
    st.session_state.skill_ativa = "E"

def mudar_pagina(nome):
    st.session_state.pagina = nome

# --- 2. ESTILIZAÇÃO CSS ---
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle, #1a1f25 0%, #0d1117 100%); }
    
    .neon-title {
        font-size: 50px; font-weight: 900; color: #00ffcc; text-align: center;
        text-transform: uppercase; letter-spacing: 5px;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 30px;
    }

    .stat-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 255, 204, 0.1);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        transition: 0.3s;
    }
    .stat-card:hover {
        border-color: #00ffcc;
        background: rgba(0, 255, 204, 0.08);
        transform: translateY(-3px);
    }
    .stat-label { color: #888; font-size: 11px; text-transform: uppercase; margin-bottom: 5px; font-weight: bold; }
    .stat-value { color: #fff; font-size: 16px; font-weight: bold; font-family: 'monospace'; }

    .class-name { font-size: 55px; font-weight: 800; color: #fff; margin: 0; line-height: 1; }
    
    .lore-box { 
        font-style: italic; color: #bbb; border-left: 3px solid #00ffcc; 
        padding-left: 15px; margin: 25px 0; line-height: 1.6;
    }

    .skill-desc-box { 
        background: rgba(0,0,0,0.4); 
        border: 1px solid #333; 
        padding: 25px; 
        border-radius: 12px; 
        border-left: 5px solid #00ffcc;
        margin-top: 20px;
    }

    div.stButton > button {
        min-height: 65px !important;
        font-weight: bold !important;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. BANCO DE DADOS (Caminhos de Imagem Atualizados) ---
CLASSES_DB = {
    "Tier 1": {
        "Swordmaster": {
            "equip": "1x Longsword", "lvl": 1, "hp_mult": "x1.0", "aggro": "x1.0",
            # CAMINHO LOCAL DA IMAGEM:
            "img": "assets/class/swordmaster.png",
            "lore": "Nascido pra empunhar a espada, o Mestre da Espada acerta seus inimigos direto no coração! Golpeie com fúria e foco pra reinar absoluto, amassando geral!.",
            "skills": {
                "E": {"nome": "Crescent Strike", "cd": "5s", "desc": "Lançe um ataque crescente contra seus inimigos."},
                "R": {"nome": "Leap Dash", "cd": "8s", "desc": "Salte em direção aos seus inimigos e desfira um golpe poderoso."},
                "X": {"nome": "Sword Cyclone", "cd": "30-200s", "desc": "Gire rapidamente criando um Ciclone que causa dano em todas as direções. Todos os golpes são ACERTOS CRÍTICOS."},
                "C": {"nome": "Dash", "cd": "2s", "desc": "Dê um impulso para a direção que o personagem estiver olhando."}
            }
        },
        "Arcane Mage": {
            "equip": "Staff", "lvl": 1, "hp_mult": "x0.8", "aggro": "x0.5",
            "img": "https://i.imgur.com/ArW80nS.png", # Mantive este online até você ter a imagem local
            "lore": "Master of arcane energies, capable of destroying armies from afar with elemental fury.",
            "skills": {
                "E": {"nome": "Meteor", "cd": "15s", "desc": "Summons a meteor at the target location."},
                "R": {"nome": "Overload", "cd": "50s", "desc": "Releases all mana in a massive burst."},
                "X": {"nome": "Blink", "cd": "5s", "desc": "Teleports a short distance forward."},
                "C": {"nome": "Arcane Bolt", "cd": "2s", "desc": "Fires a basic bolt of magic."}
            }
        }
    }
}

# --- 4. INTERFACE ---
if st.session_state.pagina == 'Home':
    st.markdown('<p class="neon-title">WORLD ZERO DATABASE</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (icon, nome) in enumerate([("🛡️", "Builds"), ("⚔️", "Classes"), ("🐾", "Pets"), ("🗺️", "Mundos")]):
        with cols[i]:
            if st.button(f"{icon} {nome}", use_container_width=True):
                mudar_pagina(nome); st.rerun()

elif st.session_state.pagina == 'Classes':
    st.button("⬅️ Menu", on_click=mudar_pagina, args=('Home',))
    
    tiers = list(CLASSES_DB.keys())
    abas = st.tabs(tiers)

    for idx, tier_nome in enumerate(tiers):
        with abas[idx]:
            classes = list(CLASSES_DB[tier_nome].keys())
            c_sel = st.columns(len(classes))
            for j, nome_c in enumerate(classes):
                with c_sel[j]:
                    if st.button(nome_c, key=f"btn_{tier_nome}_{nome_c}", use_container_width=True,
                                 type="primary" if st.session_state.classe_selecionada == nome_c else "secondary"):
                        st.session_state.classe_selecionada = nome_c
                        st.session_state.skill_ativa = "E"
                        st.rerun()

    dados = None
    tier_atual = "Tier 1"
    for t in CLASSES_DB:
        if st.session_state.classe_selecionada in CLASSES_DB[t]:
            dados = CLASSES_DB[t][st.session_state.classe_selecionada]
            tier_atual = t
            break

    if dados:
        st.divider()
        col_info, col_img = st.columns([1.6, 1])

        with col_info:
            st.markdown(f'<h1 class="class-name">{st.session_state.classe_selecionada}</h1>', unsafe_allow_html=True)
            st.markdown(f'<p style="color:#00ffcc; letter-spacing:2px; font-weight:bold; margin-bottom:20px;">{tier_atual.upper()}</p>', unsafe_allow_html=True)
            
            st.write("#### 📊 Ficha Técnica")
            g1, g2, g3, g4 = st.columns(4)
            with g1:
                st.markdown(f'<div class="stat-card"><div class="stat-label">Equipamento</div><div class="stat-value">{dados["equip"]}</div></div>', unsafe_allow_html=True)
            with g2:
                st.markdown(f'<div class="stat-card"><div class="stat-label">Mínimo Level Requerido</div><div class="stat-value">{dados["lvl"]}</div></div>', unsafe_allow_html=True)
            with g3:
                st.markdown(f'<div class="stat-card"><div class="stat-label">Multiplicador HP</div><div class="stat-value">{dados["hp_mult"]}</div></div>', unsafe_allow_html=True)
            with g4:
                st.markdown(f'<div class="stat-card"><div class="stat-label">Aggro Scaling</div><div class="stat-value">{dados["aggro"]}</div></div>', unsafe_allow_html=True)

            st.markdown(f'<div class="lore-box">{dados["lore"]}</div>', unsafe_allow_html=True)

            st.write("### ⚡ Habilidades")
            ordem = ["E", "R", "X", "C"] if tier_atual == "Tier 1" else ["E", "R", "F", "X", "C"]
            c_btns = st.columns(len(ordem))
            
            for k, tecla in enumerate(ordem):
                with c_btns[k]:
                    s_data = dados['skills'].get(tecla)
                    if st.button(f"{tecla}\n{s_data['nome']}", key=f"sk_{tecla}", use_container_width=True,
                                 type="primary" if st.session_state.skill_ativa == tecla else "secondary"):
                        st.session_state.skill_ativa = tecla
                        st.rerun()

            s_info = dados['skills'][st.session_state.skill_ativa]
            st.markdown(f"""
                <div class="skill-desc-box">
                    <h3 style='margin:0; color:#00ffcc;'>{s_info['nome']}</h3>
                    <p style='margin-top:10px; color:#eee;'>{s_info['desc']}</p>
                    <code style='color:#00ffcc; background:transparent;'>COOLDOWN: {s_info['cd']}</code>
                </div>
            """, unsafe_allow_html=True)

        with col_img:
            st.write("##") # Espaçamento para alinhar
            # O Streamlit detecta automaticamente se é um caminho de arquivo ou URL
            if os.path.exists(dados["img"]):
                st.image(dados["img"], use_container_width=True)
            else:
                # Caso o arquivo não seja encontrado, ele tenta carregar como URL ou mostra erro amigável
                st.image(dados["img"], use_container_width=True)