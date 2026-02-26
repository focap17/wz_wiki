import streamlit as st
from database import BUILDS_DB, PERKS_DB
from styles import apply_styles

st.set_page_config(page_title="Build Planner", layout="wide")
apply_styles()


def render_perks(lista_perks, categoria):
    html = ""
    for i, nome in enumerate(lista_perks):
        p = PERKS_DB.get(categoria, {}).get(nome, {"d": "...", "v": "0%"})
        cor = "#ffd700" if i == 2 else "#fff"
        html += f"""<div style="background:rgba(0,0,0,0.2); border-radius:8px; padding:10px; margin-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">
                    <div style="font-size:10px; color:#aaa; display:flex; justify-content:space-between;"><span>Perk {i+1}</span><span style="color:#ff8c00; font-weight:bold;">{p['v']}</span></div>
                    <div style="font-size:16px; font-weight:bold; margin:2px 0; color:{cor};">{nome}</div>
                    <div style="font-size:10px; color:#ccc; line-height:1.2;">{p['d']}</div></div>"""
    return html


if st.button("⬅️ VOLTAR AO MENU PRINCIPAL"):
    st.switch_page("home.py")

st.markdown('<p class="neon-title">Build Planner</p>', unsafe_allow_html=True)

if 'build_tipo' not in st.session_state:
    st.session_state.build_tipo = "FULL DPS"
if 'classe_build_selecionada' not in st.session_state:
    st.session_state.classe_build_selecionada = None

cats = list(BUILDS_DB.keys())
c_cols = st.columns(len(cats) + 2)
for i, cat in enumerate(cats):
    with c_cols[i]:
        is_active = (st.session_state.build_tipo == cat)
        if st.button(cat, key=f"bt_{cat}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.build_tipo = cat
            st.session_state.classe_build_selecionada = None
            st.rerun()

st.divider()
b_data = BUILDS_DB.get(st.session_state.build_tipo)

if b_data:
    recomendadas = b_data.get("classes_recomendadas", [])
    class_cols = st.columns(len(recomendadas) + 1)
    for i, cl_nome in enumerate(recomendadas):
        with class_cols[i]:
            is_sel = (st.session_state.classe_build_selecionada == cl_nome)
            if st.button(cl_nome, key=f"bcl_{cl_nome}", use_container_width=True, type="primary" if is_sel else "secondary"):
                st.session_state.classe_build_selecionada = cl_nome
                st.rerun()

    if st.session_state.classe_build_selecionada:
        st.divider()
        cm, cs = st.columns([3, 1])
        with cm:
            st.write(
                f"### 🛡️ Set Equipado: {st.session_state.classe_build_selecionada}")
            c1, c2, c3 = st.columns(3)
            with c1:
                for w in b_data.get("weapons", []):
                    st.markdown(f"""<div class="build-card-container" style="border-left: 4px solid #ff4b4b;"><div style="font-size:9px;color:#ff4b4b;font-weight:bold;margin-bottom:5px;">{w['tipo']}</div>
                        <div class="header-row"><div class="item-icon weapon"></div><div><b>{w['nome']}</b><br><small style="color:#00ffff;">{w['stars']}</small></div></div>
                        {render_perks(w['perks'], "Weapon")}</div>""", unsafe_allow_html=True)
            with c2:
                arm = b_data.get("armor", {})
                st.markdown(f"""<div class="build-card-container"><div style="font-size:9px;color:#00ffcc;font-weight:bold;margin-bottom:5px;">Body Gear</div>
                    <div class="header-row"><div class="item-icon"></div><div><b>{arm['nome']}</b><br><small style="color:#00ffff;">{arm['stars']}</small></div></div>
                    {render_perks(arm['perks'], "Armor")}</div>""", unsafe_allow_html=True)
            with c3:
                pt = b_data.get("pet", {})
                st.markdown(f"""<div class="build-card-container" style="border-left: 4px solid #ffcc00;"><div style="font-size:9px;color:#ffcc00;font-weight:bold;margin-bottom:5px;">Companion</div>
                    <div class="header-row"><div class="item-icon pet"></div><div><b>{pt['nome']}</b><br><small style="color:#00ffff;">{pt['stars']}</small></div></div>
                    {render_perks(pt['perks'], "Pet")}</div>""", unsafe_allow_html=True)
        with cs:
            st.write("### 📊 Performance")
            for s, v in b_data.get("stats", {}).items():
                st.write(f"**{s}**")
                st.progress(v/100)
    else:
        st.info("☝️ Selecione uma classe para carregar a Build.")
