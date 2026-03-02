import streamlit as st
import json
import os
from interface import aplicar_estilo, exibir_cabecalho, exibir_nav

# 1. Configuração da Página
st.set_page_config(page_title="Builds - W//Z Wiki",
                   layout="wide", page_icon="🛡️")

# 2. Carregar Dados


def carregar_dados():
    if not os.path.exists('database.json'):
        return {"home": {}, "builds": [], "pets": [], "perks_disponiveis": {}}
    with open('database.json', 'r', encoding='utf-8') as f:
        return json.load(f)


dados = carregar_dados()

# --- APLICANDO A INTERFACE PADRONIZADA ---
aplicar_estilo()
exibir_cabecalho(dados)
exibir_nav("BUILDS")

# --- SISTEMA DE FILTROS (HUD COMPACTO) ---
if "filtro_tag" not in st.session_state:
    st.session_state.filtro_tag = "TODAS"
if "filtro_classe" not in st.session_state:
    st.session_state.filtro_classe = "TODAS"

# Container da Barra de Filtros
with st.container():
    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)

    col_f1, col_f2 = st.columns([2.5, 1])

    with col_f1:
        st.markdown('<p class="filter-label">🔍 TIPO DE BUILD</p>',
                    unsafe_allow_html=True)
        tags_f = ["TODAS", "DPS", "Tank", "Suporte", "Eventos", "SpeedFarm"]
        c_tags = st.columns(len(tags_f))
        for i, t in enumerate(tags_f):
            is_active = st.session_state.filtro_tag == t
            # Usamos o tipo 'secondary' para o botão ativo (estilizado no interface.py)
            if c_tags[i].button(t, key=f"t_{t}", use_container_width=True,
                                type="secondary" if is_active else "primary"):
                st.session_state.filtro_tag = t
                st.rerun()

    with col_f2:
        st.markdown('<p class="filter-label">⚔️ SELECIONAR CLASSE</p>',
                    unsafe_allow_html=True)
        classes = ["TODAS"] + \
            sorted(list(set([b['classe'] for b in dados.get("builds", [])])))
        idx_atual = classes.index(
            st.session_state.filtro_classe) if st.session_state.filtro_classe in classes else 0

        classe_sel = st.selectbox(
            "", classes, index=idx_atual, label_visibility="collapsed")
        if classe_sel != st.session_state.filtro_classe:
            st.session_state.filtro_classe = classe_sel
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# Indicador de Filtro Ativo (Sutil)
st.markdown(f"""
    <div style="text-align:right; margin-bottom: 20px;">
        <span style="font-size:10px; color:#4a3f10; border:1px solid #4a3f10; padding:3px 10px; border-radius:4px; letter-spacing:1px;">
            FILTRANDO: {st.session_state.filtro_tag} | {st.session_state.filtro_classe}
        </span>
    </div>
""", unsafe_allow_html=True)

# --- LÓGICA DE FILTRAGEM ---
builds_filtradas = dados.get("builds", [])
if st.session_state.filtro_tag != "TODAS":
    builds_filtradas = [
        b for b in builds_filtradas if st.session_state.filtro_tag in b.get("tags", [])]
if st.session_state.filtro_classe != "TODAS":
    builds_filtradas = [
        b for b in builds_filtradas if b['classe'] == st.session_state.filtro_classe]

# --- EXIBIÇÃO DAS BUILDS ---
if not builds_filtradas:
    st.info("Nenhuma build encontrada com estes filtros.")
else:
    for b in builds_filtradas:
        with st.container():
            # Card de título (Simetria Master)
            st.markdown(f"""
                <div class="content-card">
                    <h2 style="color:#f1c40f; margin:0; font-size: 16px; font-family: 'Rajdhani';">{b['nome']}</h2>
                    <p style="color:#666; font-size: 10px; margin:0; letter-spacing:1px;">AUTOR: {b.get('autor', 'N/A').upper()} | KIT: {b.get('kit', 'N/A').upper()}</p>
                </div>
            """, unsafe_allow_html=True)

            col_vid, col_txt = st.columns([1, 1.4])

            with col_vid:
                if b.get("video"):
                    st.video(b["video"])
                else:
                    st.info("Vídeo não disponível")
                with st.expander("📖 DICAS DA BUILD"):
                    st.write(b.get('desc', 'Sem descrição.'))

            # --- SEÇÃO DE PERKS (DENTRO DO LOOP FOR B IN BUILDS_FILTRADAS) ---
            with col_txt:
                st.markdown(
                    "<p style='color:#f1c40f; font-weight:bold; margin-bottom:-10px;'>✨ PERKS UTILIZADOS</p>", unsafe_allow_html=True)
                p = b.get("perks", {})

                # Função auxiliar para gerar o HTML das tags de perks
                def gerar_perks_html(perks):
                    if not perks:
                        return '<span style="color:#666; font-size:11px;">---</span>'

                    # Filtra perks válidos (diferentes de "-")
                    perks_valido = [pk for pk in perks if pk != "-"]

                    if not perks_valido:
                        return '<span style="color:#666; font-size:11px;">---</span>'

                    # Gera o HTML para cada perk individual como uma tag `.perk-tag`
                    tags_html = "".join(
                        [f'<div class="perk-tag">{pk}</div>' for pk in perks_valido])

                    # Retorna o HTML envolto em um container flexbox `.perks-display-area`
                    return f'<div class="perks-display-area">{tags_html}</div>'

                # --- EXIBIÇÃO ORGANIZADA ---
                # Usamos colunas fixas para Arma 1/Arma 2 na esquerda e Armadura/Pet na direita
                c_grid_1, c_grid_2 = st.columns(2)

                # Coluna 1: Armas
                with c_grid_1:
                    # Arma 1
                    arma1 = p.get("armas", [[]])[0] if len(
                        p.get("armas", [])) > 0 else []
                    st.markdown(
                        f'<div class="perks-section-title">⚔️ Arma Primária</div>', unsafe_allow_html=True)
                    st.markdown(gerar_perks_html(arma1),
                                unsafe_allow_html=True)

                    # Arma 2
                    arma2 = p.get("armas", [[]])[1] if len(
                        p.get("armas", [])) > 1 else []
                    st.markdown(
                        f'<div class="perks-section-title">⚔️ Arma Secundária</div>', unsafe_allow_html=True)
                    st.markdown(gerar_perks_html(arma2),
                                unsafe_allow_html=True)

                # Coluna 2: Armadura e Pet
                with c_grid_2:
                    # Armadura
                    armadura = p.get("armadura", [])
                    st.markdown(
                        '<div class="perks-section-title">🛡️ Armadura</div>', unsafe_allow_html=True)
                    st.markdown(gerar_perks_html(armadura),
                                unsafe_allow_html=True)

                    # Pet
                    pet = p.get("pet", [])
                    st.markdown(
                        '<div class="perks-section-title">🐾 Pet</div>', unsafe_allow_html=True)
                    st.markdown(gerar_perks_html(pet), unsafe_allow_html=True)

        # Divisor tracejado entre as builds
        st.markdown('<div class="divisor-tracejado"></div>',
                    unsafe_allow_html=True)

        # Divisor Tracejado entre as builds
        st.markdown('<div class="divisor-tracejado"></div>',
                    unsafe_allow_html=True)
