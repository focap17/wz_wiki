import streamlit as st
from database import CLASSES_DB
from styles import apply_styles

st.set_page_config(page_title="Classes & Tiers", layout="wide")
apply_styles()

if 'classe_selecionada' not in st.session_state:
    st.session_state.classe_selecionada = "Swordmaster"
if 'skill_ativa' not in st.session_state:
    st.session_state.skill_ativa = "E"

if st.button("⬅️ VOLTAR AO MENU PRINCIPAL"):
    st.switch_page("home.py")

st.markdown('<p class="neon-title">Classes & Tiers</p>',
            unsafe_allow_html=True)

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
        st.image(dados.get(
            "img", "https://via.placeholder.com/400x600.png?text=No+Image"), use_container_width=True)
