import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="World Zero Wiki", layout="wide", page_icon="⚔️")

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Home'
if 'classe_selecionada' not in st.session_state:
    st.session_state.classe_selecionada = "Swordmaster"
if 'skill_ativa' not in st.session_state:
    st.session_state.skill_ativa = "Ataque Básico"


def mudar_pagina(nome):
    st.session_state.pagina = nome


# --- 2. ESTILIZAÇÃO CSS ---
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle, #1a1f25 0%, #0d1117 100%); }
    .neon-title {
        font-size: 50px; font-weight: 900; color: #00ffcc; text-align: center;
        text-transform: uppercase; letter-spacing: 5px;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 0;
    }
    .weapon-tag { color: #00ffcc; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; }
    .class-name { font-size: 50px; font-weight: 800; color: #fff; margin: 0; }
    .health-grid { display: flex; gap: 8px; margin-bottom: 25px; }
    .h-block { width: 40px; height: 12px; border-radius: 2px; border: 1px solid #000; }
    .h-on { background: #00ff44; box-shadow: 0 0 10px rgba(0, 255, 68, 0.4); }
    .h-off { background: #333; }
    .skill-desc-box { background: rgba(0,0,0,0.3); border: 1px solid #333; padding: 20px; border-radius: 10px; border-left: 5px solid #00ffcc; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #1e1e1e; border-radius: 5px 5px 0 0; padding: 10px 20px; color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. BANCO DE DADOS COMPLETO (TIERS 1-5 + MASTERY) ---
# Adicionei um padrão para todas, você só precisa editar os valores internos.
CLASSES_DB = {
    "Tier 1": {
        "Swordmaster": {"arma": "Longsword", "vida": 4, "lore": "Expert of the blade.", "skills": {"Ataque Básico": {"cd": "0s", "desc": "Slash!", "icon": "⚔️"}}},
        "Arcane Mage": {"arma": "Staff", "vida": 2, "lore": "Arcane power.", "skills": {"Magic Missile": {"cd": "0s", "desc": "Zap!", "icon": "🔮"}}},
        "Defender": {"arma": "Shield & Hammer", "vida": 5, "lore": "The wall.", "skills": {"Block": {"cd": "2s", "desc": "Defend!", "icon": "🛡️"}}},
    },
    "Tier 2": {
        "Dualwielder": {"arma": "Dual Sabers", "vida": 3, "lore": "Double the blades.", "skills": {"Spin": {"cd": "5s", "desc": "Wheee!", "icon": "⚔️"}}},
        "Elementalist": {"arma": "Staff", "vida": 2, "lore": "All elements.", "skills": {"Blast": {"cd": "8s", "desc": "Boom!", "icon": "🌪️"}}},
        "Guardian": {"arma": "Greatsword", "vida": 5, "lore": "Protector.", "skills": {"Taunt": {"cd": "10s", "desc": "Hey!", "icon": "🛡️"}}},
    },
    "Tier 3": {
        "Paladin": {"arma": "Mace", "vida": 5, "lore": "Holy warrior.", "skills": {"Heal": {"cd": "12s", "desc": "Light!", "icon": "✨"}}},
        "Mage of Light": {"arma": "Staff", "vida": 2, "lore": "Brilliant spells.", "skills": {"Beam": {"cd": "6s", "desc": "Flash!", "icon": "☀️"}}},
        "Berserker": {"arma": "Great Axe", "vida": 4, "lore": "Pure rage.", "skills": {"Enrage": {"cd": "20s", "desc": "Aaaargh!", "icon": "💢"}}},
    },
    "Tier 4": {
        "Deemon": {"arma": "Scythe", "vida": 4, "lore": "Infernal power.", "skills": {"Soul Trap": {"cd": "10s", "desc": "Gotcha.", "icon": "🔥"}}},
        "Dragoon": {"arma": "Spear", "vida": 4, "lore": "Dragon slayer.", "skills": {"Jump": {"cd": "7s", "desc": "High!", "icon": "🐲"}}},
        "Spirit Archer": {"arma": "Bow", "vida": 3, "lore": "Spectral arrows.", "skills": {"Rain": {"cd": "9s", "desc": "Arrow rain.", "icon": "🏹"}}},
    },
    "Tier 5": {
        "Summoner": {"arma": "Book", "vida": 3, "lore": "Calls minions.", "skills": {"Summon": {"cd": "15s", "desc": "Rise!", "icon": "🐾"}}},
        "Warlord": {"arma": "Heavy Blade", "vida": 5, "lore": "Battle master.", "skills": {"Charge": {"cd": "8s", "desc": "Go!", "icon": "🚩"}}},
        "Shadowblade": {"arma": "Daggers", "vida": 3, "lore": "Hidden killer.", "skills": {"Stealth": {"cd": "12s", "desc": "...", "icon": "🌑"}}},
    },
    "Mastery": {
        "Mage of Shadows": {"arma": "Shadow Staff", "vida": 3, "lore": "Dark arts.", "skills": {"Void": {"cd": "10s", "desc": "Nothingness.", "icon": "🌑"}}},
        "Necromancer": {"arma": "Scythe", "vida": 3, "lore": "Dead riser.", "skills": {"Undead": {"cd": "20s", "desc": "Live!", "icon": "💀"}}},
        "Stormcaller": {"arma": "Staff", "vida": 2, "lore": "Lightning master.", "skills": {"Thunder": {"cd": "5s", "desc": "Zap!", "icon": "⚡"}}},
        "Hunter": {"arma": "Crossbow", "vida": 3, "lore": "Primal tracker.", "skills": {"Trap": {"cd": "8s", "desc": "Stay.", "icon": "🪤"}}},
        "Starbreaker": {"arma": "Cosmic Blade", "vida": 4, "lore": "Galaxy power.", "skills": {"Nova": {"cd": "15s", "desc": "Star!", "icon": "⭐"}}},
        "Leviathan": {"arma": "Trident", "vida": 5, "lore": "Deep sea king.", "skills": {"Wave": {"cd": "12s", "desc": "Splash!", "icon": "🌊"}}},
    }
}

# --- 4. LÓGICA DE NAVEGAÇÃO ---
if st.session_state.pagina == 'Home':
    st.markdown('<p class="neon-title">WORLD ZERO</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    menu = [("🛡️", "Builds"), ("⚔️", "Classes"),
            ("🐾", "Pets"), ("🗺️", "Mundos")]
    for i, (icon, nome) in enumerate(menu):
        with cols[i]:
            if st.button(f"{icon} {nome}", use_container_width=True):
                mudar_pagina(nome)
                st.rerun()

elif st.session_state.pagina == 'Classes':
    st.button("⬅️ Menu", on_click=mudar_pagina, args=('Home',))

    st.write("### 🏷️ Select Tier & Class")
    abas = st.tabs(list(CLASSES_DB.keys()))

    for i, tier in enumerate(CLASSES_DB.keys()):
        with abas[i]:
            classes_do_tier = list(CLASSES_DB[tier].keys())
            cols_grid = st.columns(3)  # Organizado em 3 colunas por Tier
            for j, nome_classe in enumerate(classes_do_tier):
                with cols_grid[j % 3]:
                    is_active = st.session_state.classe_selecionada == nome_classe
                    if st.button(nome_classe, key=f"btn_{nome_classe}", use_container_width=True, type="primary" if is_active else "secondary"):
                        st.session_state.classe_selecionada = nome_classe
                        st.session_state.skill_ativa = list(
                            CLASSES_DB[tier][nome_classe]['skills'].keys())[0]
                        st.rerun()

    # --- BUSCA DADOS ---
    dados = None
    for tier in CLASSES_DB:
        if st.session_state.classe_selecionada in CLASSES_DB[tier]:
            dados = CLASSES_DB[tier][st.session_state.classe_selecionada]
            break

    if dados:
        st.divider()
        col_info, col_char = st.columns([1.2, 1])
        with col_info:
            st.markdown(
                f'<span class="weapon-tag">Weapon Type: {dados["arma"]}</span>', unsafe_allow_html=True)
            st.markdown(
                f'<h1 class="class-name">{st.session_state.classe_selecionada}</h1>', unsafe_allow_html=True)

            st.markdown(
                '<span class="health-label">HEALTH / RESISTANCE</span>', unsafe_allow_html=True)
            blocos = "".join(
                ['<div class="h-block h-on"></div>' for _ in range(dados['vida'])])
            blocos += "".join(
                ['<div class="h-block h-off"></div>' for _ in range(5 - dados['vida'])])
            st.markdown(
                f'<div class="health-grid">{blocos}</div>', unsafe_allow_html=True)

            st.markdown(
                f'<div class="lore-box">{dados["lore"]}</div>', unsafe_allow_html=True)

            st.write("### ⚡ Abilities")
            c_icons = st.columns(6)
            for i, (nome_s, info_s) in enumerate(dados['skills'].items()):
                with c_icons[i]:
                    btn_type = "primary" if st.session_state.skill_ativa == nome_s else "secondary"
                    if st.button(info_s['icon'], key=f"sk_{nome_s}", type=btn_type):
                        st.session_state.skill_ativa = nome_s
                        st.rerun()

            skill_info = dados['skills'][st.session_state.skill_ativa]
            st.markdown(f"""
                <div class="skill-desc-box">
                    <h3 style='margin:0; color:#00ffcc;'>{st.session_state.skill_ativa}</h3>
                    <small style='color:#888;'>COOLDOWN: {skill_info['cd']}</small>
                    <p style='margin-top:10px; color:#eee;'>{skill_info['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

        with col_char:
            # Placeholder de imagem - aqui você pode colocar o modelo de cada classe
            st.image("https://i.imgur.com/3Z6O3Z8.png",
                     use_container_width=True)
            st.button(f"EQUIP {st.session_state.classe_selecionada.upper()}",
                      type="primary", use_container_width=True)
