import streamlit as st

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
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 0;
    }
    .weapon-tag { color: #00ffcc; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; }
    .class-name { font-size: 50px; font-weight: 800; color: #fff; margin: 0; }
    .lore-box { font-style: italic; color: #ccc; border-left: 4px solid #00ffcc; padding-left: 20px; margin: 20px 0; }
    .health-grid { display: flex; gap: 8px; margin-bottom: 25px; }
    .h-block { width: 40px; height: 12px; border-radius: 2px; border: 1px solid #000; }
    .h-on { background: #00ff44; box-shadow: 0 0 10px rgba(0, 255, 68, 0.4); }
    .h-off { background: #333; }
    .skill-desc-box { background: rgba(0,0,0,0.3); border: 1px solid #333; padding: 20px; border-radius: 10px; border-left: 5px solid #00ffcc; }
    .key-hint { text-align: center; color: #00ffcc; font-size: 14px; font-weight: bold; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# --- 3. BANCO DE DADOS (ORDEM DAS SKILLS: E, R, F, X, Q) ---
CLASSES_DB = {
    "Tier 1": {
        "Swordmaster": {
            "arma": "Longsword", "vida": 4, "img": "https://i.imgur.com/3Z6O3Z8.png",
            "lore": "A versatile fighter proficient with blades.",
            "skills": {
                "E": {"nome": "Blade Whirl", "cd": "12s", "desc": "Spin around dealing AOE damage."},
                "R": {"nome": "Ultimate Slash", "cd": "60s", "desc": "A devastating finishing move."},
                "F": {"nome": "Guard", "cd": "8s", "desc": "Reduces damage taken from the front."},
                "X": {"nome": "Skill Especial", "cd": "20s", "desc": "Habilidade secundária da classe."},
                "Q": {"nome": "Leaping Slash", "cd": "6s", "desc": "A leap forward with a heavy strike."}
            }
        },
        "Arcane Mage": {
            "arma": "Staff", "vida": 2, "img": "https://i.imgur.com/ArW80nS.png",
            "lore": "Harnesses raw arcane energy.",
            "skills": {
                "E": {"nome": "Meteor", "cd": "15s", "desc": "Calls down a giant rock."},
                "R": {"nome": "Arcane Overload", "cd": "50s", "desc": "Massive burst of energy."},
                "F": {"nome": "Mana Shield", "cd": "12s", "desc": "Uses mana to block damage."},
                "X": {"nome": "Blink", "cd": "5s", "desc": "Short teleport."},
                "Q": {"nome": "Arcane Bolt", "cd": "2s", "desc": "Rapid magic projectiles."}
            }
        },
        "Defender": {
            "arma": "Shield & Hammer", "vida": 5, "img": "https://i.imgur.com/M6LgT77.png",
            "lore": "A sturdy tank that protects allies.",
            "skills": {
                "E": {"nome": "Fortify", "cd": "20s", "desc": "Greatly increases defense."},
                "R": {"nome": "Earthquake", "cd": "45s", "desc": "Stuns all nearby enemies."},
                "F": {"nome": "Taunt", "cd": "10s", "desc": "Forces enemies to attack you."},
                "X": {"nome": "Shield Wall", "cd": "15s", "desc": "Creates a protective barrier."},
                "Q": {"nome": "Shield Charge", "cd": "8s", "desc": "Dashes forward pushing enemies."}
            }
        }
    },
    "Tier 2": {"Dualwielder": {"arma": "Dual Sabers", "vida": 3, "img": "https://i.imgur.com/x8P2P4k.png", "lore": "Fast and agile.", "skills": {"E": {"nome": "Spin", "cd": "5s", "desc": "Double strike."}}}},
    "Tier 3": {"Paladin": {"arma": "Mace", "vida": 5, "img": "https://i.imgur.com/3Z6O3Z8.png", "lore": "Holy warrior.", "skills": {"E": {"nome": "Smite", "cd": "10s", "desc": "Holy hit."}}}},
    "Tier 4": {"Deemon": {"arma": "Scythe", "vida": 4, "img": "https://i.imgur.com/3Z6O3Z8.png", "lore": "Dark arts.", "skills": {"E": {"nome": "Soul Reap", "cd": "12s", "desc": "Steals life."}}}},
    "Tier 5": {"Summoner": {"arma": "Book", "vida": 3, "img": "https://i.imgur.com/ArW80nS.png", "lore": "Calls minions.", "skills": {"E": {"nome": "Call", "cd": "20s", "desc": "Summon pet."}}}},
    "Mastery": {"Leviathan": {"arma": "Trident", "vida": 5, "img": "https://i.imgur.com/M6LgT77.png", "lore": "Abyssal King.", "skills": {"E": {"nome": "Tidal Wave", "cd": "18s", "desc": "Giant wave."}}}}
}

# --- 4. NAVEGAÇÃO ---
if st.session_state.pagina == 'Home':
    st.markdown('<p class="neon-title">WORLD ZERO</p>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (icon, nome) in enumerate([("🛡️", "Builds"), ("⚔️", "Classes"), ("🐾", "Pets"), ("🗺️", "Mundos")]):
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
            classes = list(CLASSES_DB[tier].keys())
            cols_grid = st.columns(3)
            for j, nome_c in enumerate(classes):
                with cols_grid[j % 3]:
                    if st.button(nome_c, key=f"sel_{nome_c}", use_container_width=True,
                                 type="primary" if st.session_state.classe_selecionada == nome_c else "secondary"):
                        st.session_state.classe_selecionada = nome_c
                        # Garante que a primeira tecla da nova classe seja selecionada
                        st.session_state.skill_ativa = list(
                            CLASSES_DB[tier][nome_c]['skills'].keys())[0]
                        st.rerun()

    # Busca Dados
    dados = None
    for tier in CLASSES_DB:
        if st.session_state.classe_selecionada in CLASSES_DB[tier]:
            dados = CLASSES_DB[tier][st.session_state.classe_selecionada]
            break

    if dados:
        st.divider()
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.markdown(
                f'<span class="weapon-tag">Weapon: {dados["arma"]}</span>', unsafe_allow_html=True)
            st.markdown(
                f'<h1 class="class-name">{st.session_state.classe_selecionada}</h1>', unsafe_allow_html=True)

            blocos = "".join(
                ['<div class="h-block h-on"></div>' for _ in range(dados['vida'])])
            blocos += "".join(
                ['<div class="h-block h-off"></div>' for _ in range(5 - dados['vida'])])
            st.markdown(
                f'<div class="health-grid">{blocos}</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="lore-box">{dados["lore"]}</div>', unsafe_allow_html=True)

            # --- SELETOR DE SKILLS POR TECLAS (ORDEM E, R, F, X, Q) ---
            st.write("### ⌨️ Abilities Hotkeys")
            ordem_teclas = ["E", "R", "F", "X", "Q"]
            c_keys = st.columns(len(ordem_teclas))

            for k, tecla in enumerate(ordem_teclas):
                with c_keys[k]:
                    if tecla in dados['skills']:
                        is_active = st.session_state.skill_ativa == tecla
                        if st.button(tecla, key=f"key_{tecla}", use_container_width=True,
                                     type="primary" if is_active else "secondary"):
                            st.session_state.skill_ativa = tecla
                            st.rerun()
                    else:
                        st.button(tecla, disabled=True,
                                  use_container_width=True)

            # Info da Skill Selecionada
            s_info = dados['skills'].get(st.session_state.skill_ativa, {
                                         "nome": "N/A", "desc": "N/A", "cd": "N/A"})
            st.markdown(f"""
                <div class="skill-desc-box">
                    <h3 style='margin:0; color:#00ffcc;'>{s_info['nome']} <small style='color:#666'>( {st.session_state.skill_ativa} )</small></h3>
                    <p style='margin-top:10px; color:#eee;'>{s_info['desc']}</p>
                    <small style='color:#00ffcc; font-weight:bold;'>COOLDOWN: {s_info['cd']}</small>
                </div>
            """, unsafe_allow_html=True)

        with c2:
            st.image(dados['img'], use_container_width=True)
            st.button(f"EQUIP {st.session_state.classe_selecionada.upper()}",
                      type="primary", use_container_width=True)
