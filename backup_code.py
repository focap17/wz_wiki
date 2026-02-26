import streamlit as st

# =================================================================
# [ESTRUTURA 1] CONFIGURAÇÕES GERAIS E ESTADO DO SISTEMA
# =================================================================
st.set_page_config(page_title="World Zero Wiki", layout="wide", page_icon="⚔️")

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Home'
if 'classe_selecionada' not in st.session_state:
    st.session_state.classe_selecionada = "Swordmaster"
if 'skill_ativa' not in st.session_state:
    st.session_state.skill_ativa = "E"
if 'build_tipo' not in st.session_state:
    st.session_state.build_tipo = "FULL DPS"
if 'classe_build_selecionada' not in st.session_state:
    st.session_state.classe_build_selecionada = None


def mudar_pagina(nome):
    st.session_state.pagina = nome
    st.session_state.classe_build_selecionada = None


# =================================================================
# [ESTRUTURA 2] BANCO DE DADOS DE PERKS (BUILD)
# =================================================================
PERKS_DB = {
    "Armor": {
        "HP UP": {"d": "Aumenta significativamente seus pontos de vida.", "v": "11% (S)"},
        "Rough Skin": {"d": "Chance de refletir dano recebido.", "v": "9% (S)"},
        "Fortress": {"d": "Grande bônus de defesa.", "v": "39% (S)"},
        "Attack UP": {"d": "Aumenta o dano total causado.", "v": "15% (S)"},
        "Critical Eye": {"d": "Aumenta a chance de críticos.", "v": "12% (S)"},
        "Brawler": {"d": "Dano extra próximo a inimigos.", "v": "45% (S)"}
    },
    "Weapon": {
        "Boss Damage": {"d": "Dano massivo contra chefes.", "v": "25% (S)"},
        "Executioner": {"d": "Dano extra a inimigos com pouco HP.", "v": "50% (S)"},
        "Lifesteal": {"d": "Recupera HP a cada golpe.", "v": "5% (S)"},
        "Stun Hit": {"d": "Chance de atordoar o alvo.", "v": "8% (S)"},
        "Block Rate": {"d": "Aumenta chance de mitigar dano.", "v": "15% (S)"}
    },
    "Pet": {
        "Burn Aura": {"d": "Dano de fogo ao redor do pet.", "v": "Lvl 50"},
        "Fire Mastery": {"d": "Fortalece elemento fogo.", "v": "Max"},
        "Shell": {"d": "Barreira que reduz o dano.", "v": "S"},
        "Taunt": {"d": "Atrai atenção dos monstros.", "v": "Max"}
    }
}

# =================================================================
# [ESTRUTURA 3] BANCO DE DADOS DE BUILDS
# =================================================================
BUILDS_DB = {
    "FULL DPS": {
        "stats": {"Dano": 98, "Defesa": 25, "Velocidade": 65, "Sorte": 30},
        "classes_recomendadas": ["Swordmaster", "Arcane Mage", "Dualwilder"],
        "armor": {"nome": "Zero Armor", "stars": "★★★★★★", "perks": ["Attack UP", "Critical Eye", "Brawler"]},
        "weapons": [{"nome": "Void Blade", "stars": "★★★★★★", "tipo": "Primary Weapon", "perks": ["Boss Damage", "Executioner", "Lifesteal"]}],
        "pet": {"nome": "Phoenix", "stars": "★★★★★", "perks": ["Burn Aura", "Fire Mastery", "Attack UP"]}
    },
    "FULL TANK": {
        "stats": {"Dano": 35, "Defesa": 100, "Velocidade": 30, "Sorte": 45},
        "classes_recomendadas": ["Defender", "Guardian"],
        "armor": {"nome": "Guardian Plate", "stars": "★★★★★★", "perks": ["HP UP", "Rough Skin", "Fortress"]},
        "weapons": [{"nome": "Bulwark Hammer", "stars": "★★★★★★", "tipo": "Main Hand", "perks": ["Stun Hit", "Lifesteal", "Block Rate"]}],
        "pet": {"nome": "Turtle", "stars": "★★★★★", "perks": ["Shell", "Taunt", "HP UP"]}
    }
}

# =================================================================
# [START] >>> BANCO DE DADOS DE CLASSES (TIERS E IMAGENS) <<<
# =================================================================
# DICA: O campo "img" deve conter a URL da imagem da classe.
# =================================================================
CLASSES_DB = {
    "Tier 1": {
        "Swordmaster": {
            "img": "assets/class/swordmaster.png",
            "equip": "1x Longsword", "lvl": 1, "hp_mult": "x1.0", "aggro": "x1.0",
            "lore": "Mestre da espada que foca em cortes rápidos e precisos.",
            "skills": {
                "E": {"nome": "Crescent Strike", "cd": "5s", "desc": "Ataque crescente."},
                "R": {"nome": "Leap Dash", "cd": "8s", "desc": "Salte em direção aos inimigos."},
                "X": {"nome": "Sword Cyclone", "cd": "30s", "desc": "Giro devastador com críticos."},
                "C": {"nome": "Dash", "cd": "2s", "desc": "Esquiva rápida."}
            }
        },
        "Arcane Mage": {
            "img": "assets/class/arcanemage.png",
            "equip": "Staff", "lvl": 1, "hp_mult": "x0.9", "aggro": "x1.2",
            "lore": "Mago poderoso que utiliza mana para ataques em área.",
            "skills": {
                "E": {"nome": "Arcane Blast", "cd": "5s", "desc": "Orbe explosivo de energia."},
                "R": {"nome": "Arcane Wave", "cd": "8s", "desc": "Explosões no chão."},
                "X": {"nome": "Arcane Ascension", "cd": "30s", "desc": "Orbe gigante."},
                "C": {"nome": "Dash", "cd": "2s", "desc": "Teleporte curto."}
            }
        },
        "Defender": {
            "img": "https://via.placeholder.com/400x600.png?text=Defender",
            "equip": "Shield & Hammer", "lvl": 1, "hp_mult": "x1.5", "aggro": "x2.0",
            "lore": "A muralha inquebrável que protege seus aliados.",
            "skills": {
                "E": {"nome": "Shield Bash", "cd": "6s", "desc": "Atordoa com o escudo."},
                "R": {"nome": "Iron Will", "cd": "12s", "desc": "Defesa temporária."},
                "X": {"nome": "Aegis Protection", "cd": "45s", "desc": "Redução de dano em área."},
                "C": {"nome": "Dash", "cd": "2.5s", "desc": "Avanço pesado."}
            }
        }
    },
    "Tier 2": {
        "Dualwilder": {"img": "https://via.placeholder.com/400x600.png?text=Dualwilder", "equip": "2x Swords", "lvl": 15, "hp_mult": "x1.0", "aggro": "x1.0", "lore": "Edite aqui", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}},
        "Elementalist": {"img": "https://via.placeholder.com/400x600.png?text=Elementalist", "equip": "Staff", "lvl": 15, "hp_mult": "x0.9", "aggro": "x1.2", "lore": "Edite aqui", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}},
        "Guardian": {"img": "https://via.placeholder.com/400x600.png?text=Guardian", "equip": "Shield & Sword", "lvl": 15, "hp_mult": "x1.5", "aggro": "x2.0", "lore": "Edite aqui", "skills": {"E": {"nome": "S1", "cd": "5s", "desc": "D"}, "R": {"nome": "S2", "cd": "5s", "desc": "D"}, "F": {"nome": "S3", "cd": "5s", "desc": "D"}, "X": {"nome": "S4", "cd": "5s", "desc": "D"}, "C": {"nome": "S5", "cd": "5s", "desc": "D"}}}
    },
    "Tier 3": {
        "Paladin": {"img": "https://via.placeholder.com/400x600.png?text=Paladin", "equip": "Mace", "lvl": 30, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Mage of Light": {"img": "https://via.placeholder.com/400x600.png?text=MageOfLight", "equip": "Staff", "lvl": 30, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Berserker": {"img": "https://via.placeholder.com/400x600.png?text=Berserker", "equip": "Greatsword", "lvl": 30, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Tier 4": {
        "Demon": {"img": "https://via.placeholder.com/400x600.png?text=Demon", "equip": "Scythe", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Dragon": {"img": "https://via.placeholder.com/400x600.png?text=Dragon", "equip": "Gauntlets", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Spirit Archer": {"img": "https://via.placeholder.com/400x600.png?text=SpiritArcher", "equip": "Bow", "lvl": 50, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Tier 5": {
        "Warlord": {"img": "https://via.placeholder.com/400x600.png?text=Warlord", "equip": "Sword", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Summoner": {"img": "https://via.placeholder.com/400x600.png?text=Summoner", "equip": "Staff", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Shadowblade": {"img": "https://via.placeholder.com/400x600.png?text=Shadowblade", "equip": "Daggers", "lvl": 75, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    },
    "Maestria": {
        "Shadowmage": {"img": "https://via.placeholder.com/400x600.png?text=Shadowmage", "equip": "Soul Staff", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Hunter": {"img": "assets/class/swordmaster.png", "equip": "Crossbow", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Stormcaller": {"img": "https://via.placeholder.com/400x600.png?text=Stormcaller", "equip": "Orb", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Leviathan": {"img": "https://via.placeholder.com/400x600.png?text=Leviathan", "equip": "Trident", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Starbreaker": {"img": "https://via.placeholder.com/400x600.png?text=Starbreaker", "equip": "Hammer", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}},
        "Necromancer": {"img": "https://via.placeholder.com/400x600.png?text=Necromancer", "equip": "Grimoire", "lvl": 100, "hp_mult": "1.0", "aggro": "1.0", "lore": "Lore", "skills": {"E": {"nome": "E", "cd": "5s", "desc": "D"}, "R": {"nome": "R", "cd": "5s", "desc": "D"}, "F": {"nome": "F", "cd": "5s", "desc": "D"}, "X": {"nome": "X", "cd": "5s", "desc": "D"}, "C": {"nome": "C", "cd": "5s", "desc": "D"}}}
    }
}
# =================================================================
# [END] <<< BANCO DE DADOS DE CLASSES <<<
# =================================================================

# =================================================================
# [ESTRUTURA 4] ESTILIZAÇÃO CSS
# =================================================================
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle, #1a1f25 0%, #0d1117 100%); }
    .neon-title { font-size: 50px; font-weight: 900; color: #00ffcc; text-align: center; text-transform: uppercase; letter-spacing: 5px; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 30px; }
    .stat-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 255, 204, 0.1); padding: 15px; border-radius: 10px; text-align: center; }
    .stat-label { color: #888; font-size: 11px; text-transform: uppercase; font-weight: bold; }
    .stat-value { color: #fff; font-size: 16px; font-weight: bold; }
    .class-name { font-size: 55px; font-weight: 800; color: #fff; margin: 0; }
    .skill-desc-box { background: rgba(0,0,0,0.4); border: 1px solid #333; padding: 25px; border-radius: 12px; border-left: 5px solid #00ffcc; }
    .build-card-container { background-color: #0b4c8c; border-radius: 12px; padding: 18px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.5); margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.1); }
</style>
""", unsafe_allow_html=True)

# =================================================================
# [ESTRUTURA 5] LÓGICA DE NAVEGAÇÃO
# =================================================================

if st.session_state.pagina == 'Home':
    st.markdown('<p class="neon-title">WORLD ZERO DATABASE</p>',
                unsafe_allow_html=True)
    cols = st.columns(4)
    menu = [("🛡️", "Builds"), ("⚔️", "Classes"),
            ("🐾", "Pets"), ("🗺️", "Mundos")]
    for i, (icon, nome) in enumerate(menu):
        with cols[i]:
            if st.button(f"{icon} {nome}", use_container_width=True):
                mudar_pagina(nome)
                st.rerun()

# ---------------------------------------------------------
# ABA: BUILDS (SISTEMA DE SUB-CATEGORIA CORRIGIDO)
# ---------------------------------------------------------
elif st.session_state.pagina == 'Builds':
    st.button("⬅️ Menu", on_click=mudar_pagina, args=('Home',))
    st.markdown('<p class="neon-title">Build Planner</p>',
                unsafe_allow_html=True)

    # 1. Seleção de Estilo (FULL DPS, FULL TANK, etc)
    cats = list(BUILDS_DB.keys())
    c_cols = st.columns(len(cats) + 2)
    for i, cat in enumerate(cats):
        with c_cols[i]:
            # Se o botão for o estilo ativo, ele fica em destaque (primary)
            is_active = (st.session_state.build_tipo == cat)
            if st.button(cat, key=f"bt_{cat}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state.build_tipo = cat
                # Reseta a classe ao trocar o estilo
                st.session_state.classe_build_selecionada = None
                st.rerun()

    st.divider()

    # Pega os dados do estilo selecionado (ex: FULL DPS)
    b_data = BUILDS_DB.get(st.session_state.build_tipo)

    if b_data:
        # MENSAGEM DE ORIENTAÇÃO
        st.markdown(
            f'<div class="sub-cat-title">Selecione uma classe para ver a Build de {st.session_state.build_tipo}:</div>', unsafe_allow_html=True)

        # 2. Renderiza os botões das classes recomendadas para aquele estilo
        recomendadas = b_data.get("classes_recomendadas", [])
        if recomendadas:
            class_cols = st.columns(len(recomendadas) + 1)
            for i, cl_nome in enumerate(recomendadas):
                with class_cols[i]:
                    # Verifica se esta classe é a que está selecionada no momento
                    is_sel = (
                        st.session_state.classe_build_selecionada == cl_nome)
                    if st.button(cl_nome, key=f"bcl_{cl_nome}", use_container_width=True, type="primary" if is_sel else "secondary"):
                        st.session_state.classe_build_selecionada = cl_nome
                        st.rerun()
        else:
            st.warning(
                "Nenhuma classe recomendada cadastrada para este estilo.")

        # 3. Mostrar os itens (Armor, Weapon, Pet) APENAS SE uma classe for selecionada
        if st.session_state.classe_build_selecionada:
            st.divider()
            cm, cs = st.columns([3, 1])
            with cm:
                st.write(
                    f"### 🛡️ Set Equipado: {st.session_state.classe_build_selecionada}")
                c1, c2, c3 = st.columns(3)

                with c1:  # COLUNA DAS ARMAS
                    for w in b_data.get("weapons", []):
                        st.markdown(f"""<div class="build-card-container" style="border-left: 4px solid #ff4b4b;"><div style="font-size:9px;color:#ff4b4b;font-weight:bold;margin-bottom:5px;">{w['tipo']}</div>
                            <div class="header-row"><div class="item-icon weapon"></div><div><b>{w['nome']}</b><br><small style="color:#00ffff;">{w['stars']}</small></div></div>
                            {render_perks(w['perks'], "Weapon")}</div>""", unsafe_allow_html=True)

                with c2:  # COLUNA DA ARMADURA
                    arm = b_data.get("armor", {})
                    st.markdown(f"""<div class="build-card-container"><div style="font-size:9px;color:#00ffcc;font-weight:bold;margin-bottom:5px;">Body Gear</div>
                        <div class="header-row"><div class="item-icon"></div><div><b>{arm['nome']}</b><br><small style="color:#00ffff;">{arm['stars']}</small></div></div>
                        {render_perks(arm['perks'], "Armor")}</div>""", unsafe_allow_html=True)

                with c3:  # COLUNA DO PET
                    pt = b_data.get("pet", {})
                    st.markdown(f"""<div class="build-card-container" style="border-left: 4px solid #ffcc00;"><div style="font-size:9px;color:#ffcc00;font-weight:bold;margin-bottom:5px;">Companion</div>
                        <div class="header-row"><div class="item-icon pet"></div><div><b>{pt['nome']}</b><br><small style="color:#00ffff;">{pt['stars']}</small></div></div>
                        {render_perks(pt['perks'], "Pet")}</div>""", unsafe_allow_html=True)

            with cs:  # COLUNA DAS STATS (LADO DIREITO)
                st.write("### 📊 Performance")
                for s, v in b_data.get("stats", {}).items():
                    st.markdown(
                        f'<p class="stat-text">{s}</p>', unsafe_allow_html=True)
                    st.progress(v/100)
        else:
            # Caso o usuário tenha escolhido o Estilo mas não a Classe ainda
            st.light(
                "☝️ Clique em uma das classes acima para carregar os equipamentos.")

# ---------------------------------------------------------
# [START] ABA: CLASSES (COM IMAGEM REATIVADA)
# ---------------------------------------------------------
elif st.session_state.pagina == 'Classes':
    st.button("⬅️ Menu", on_click=mudar_pagina, args=('Home',))

    # Abas de Tiers
    abas_tiers = st.tabs(list(CLASSES_DB.keys()))

    for idx, tier_nome in enumerate(CLASSES_DB.keys()):
        with abas_tiers[idx]:
            classes_do_tier = list(CLASSES_DB[tier_nome].keys())
            c_cols = st.columns(len(classes_do_tier))
            for j, nome_classe in enumerate(classes_do_tier):
                with c_cols[j]:
                    if st.button(nome_classe, key=f"btn_c_{nome_classe}", use_container_width=True,
                                 type="primary" if st.session_state.classe_selecionada == nome_classe else "secondary"):
                        st.session_state.classe_selecionada = nome_classe
                        st.session_state.skill_ativa = "E"
                        st.rerun()

    # Busca dados da classe selecionada
    dados = None
    tier_da_classe = ""
    for t in CLASSES_DB:
        if st.session_state.classe_selecionada in CLASSES_DB[t]:
            dados = CLASSES_DB[t][st.session_state.classe_selecionada]
            tier_da_classe = t
            break

    if dados:
        st.divider()
        col1, col2 = st.columns([1.6, 1])
        with col1:
            st.markdown(
                f'<h1 class="class-name">{st.session_state.classe_selecionada}</h1><p style="color:#00ffcc; font-weight:bold;">{tier_da_classe.upper()} CLASSIFICATION</p>', unsafe_allow_html=True)
            g = st.columns(4)
            for i, (l, k) in enumerate([("Equipamento", "equip"), ("Min Lvl", "lvl"), ("HP Mult", "hp_mult"), ("Aggro", "aggro")]):
                g[i].markdown(
                    f'<div class="stat-card"><div class="stat-label">{l}</div><div class="stat-value">{dados[k]}</div></div>', unsafe_allow_html=True)

            st.markdown(
                f'<div style="font-style:italic; color:#bbb; border-left:3px solid #00ffcc; padding-left:15px; margin:25px 0;">{dados["lore"]}</div>', unsafe_allow_html=True)

            st.write("### ⚡ Habilidades")
            teclas = list(dados['skills'].keys())
            h_cols = st.columns(len(teclas))
            for i, tecla in enumerate(teclas):
                with h_cols[i]:
                    if st.button(f"{tecla}\n{dados['skills'][tecla]['nome']}", key=f"vsk_{tecla}", use_container_width=True,
                                 type="primary" if st.session_state.skill_ativa == tecla else "secondary"):
                        st.session_state.skill_ativa = tecla
                        st.rerun()

            sk = dados['skills'][st.session_state.skill_ativa]
            st.markdown(
                f'<div class="skill-desc-box"><h3 style="color:#00ffcc; margin:0;">{sk["nome"]}</h3><p style="color:#eee; margin-top:10px;">{sk["desc"]}</p><code>CD: {sk["cd"]}</code></div>', unsafe_allow_html=True)

        with col2:
            st.write("### Visualização")
            # AQUI ESTÁ A IMAGEM: Ela busca o campo "img" do dicionário
            st.image(dados.get(
                "img", "https://via.placeholder.com/400x600.png?No+Image"), use_container_width=True)
# ---------------------------------------------------------
# [END] ABA: CLASSES
# ---------------------------------------------------------
