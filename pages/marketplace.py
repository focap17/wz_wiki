import streamlit as st
import json
import os
from interface import aplicar_estilo, exibir_cabecalho, exibir_nav

# 1. Configuração da Página
st.set_page_config(page_title="W//Z Wiki - Marketplace",
                   layout="wide", page_icon="🛒")

# 2. Carregar Dados


def carregar_dados():
    if not os.path.exists('database.json'):
        return {"marketplace": []}
    with open('database.json', 'r', encoding='utf-8') as f:
        return json.load(f)


dados = carregar_dados()

# --- APLICANDO A INTERFACE PADRONIZADA ---
aplicar_estilo()
exibir_cabecalho(dados)
exibir_nav("MARKET")

# --- TÍTULO DA PÁGINA ---
st.markdown('<h2 style="font-family: \'Rajdhani\'; color: #f1c40f; letter-spacing: 2px;">🛒 GUIA DE PREÇOS DA COMUNIDADE</h2>', unsafe_allow_html=True)
st.write("Consulte os valores médios de mercado e códigos de cores originais das skins.")

# --- BARRA DE FILTROS ---
col_f1, col_f2 = st.columns([2, 1])
with col_f1:
    busca = st.text_input("🔍 Procurar item pelo nome...",
                          placeholder="Ex: Soul Eater, Dragon Armor...")

with col_f2:
    categorias = ["Todos", "Aura", "Weapon Skin", "Hat", "Tail",
                  "Back", "Costume", "Mount", "Both", "Furniture"]
    cat_filtro = st.selectbox("Filtrar Categoria", categorias)

# --- LÓGICA DE FILTRAGEM ---
itens = dados.get("marketplace", [])

# Filtrar por nome e categoria
itens_filtrados = [
    i for i in itens
    if (busca.lower() in i.get('nome', '').lower()) and
    (cat_filtro == "Todos" or i.get('categoria') == cat_filtro)
]

# --- EXIBIÇÃO EM GRID ---
if not itens_filtrados:
    st.info("Nenhum item encontrado com os filtros selecionados.")
else:
    # Criar 3 colunas para os cards
    cols = st.columns(3)

    for idx, item in enumerate(itens_filtrados):
        with cols[idx % 3]:
            nome = item.get('nome', 'Sem Nome')
            categoria = item.get('categoria', 'N/A')
            preco = item.get('preco', 0)
            hex_skin = item.get('hex_original', 'N/A')
            data_att = item.get('atualizado_em', 'N/A')
            cor_preview = hex_skin if hex_skin.startswith(
                '#') else 'transparent'

            # Removi os espaços na frente das tags HTML para forçar a renderização
            st.markdown(f"""
<div class="content-card" style="border-left: 5px solid #f1c40f; margin-bottom: 20px; min-height: 220px;">
<div style="font-size: 10px; color: #888; font-weight: bold; letter-spacing: 1.5px; margin-bottom: 5px;">{categoria.upper()}</div>
<h3 style="margin: 0; font-family: 'Rajdhani'; color: #ffffff; border: none; padding: 0;">{nome.upper()}</h3>
<div style="background: rgba(241, 196, 15, 0.1); padding: 12px; border-radius: 8px; margin: 15px 0; border: 1px dashed rgba(241, 196, 15, 0.3);">
<span style="font-size: 11px; color: #aaa; font-weight: bold;">VALOR ESTIMADO:</span><br>
<span style="font-size: 22px; font-weight: bold; color: #f1c40f; font-family: 'Rajdhani';">💰 {preco:,} <span style="font-size: 14px;">GOLD</span></span>
</div>
<div style="display: flex; align-items: center; gap: 8px; font-family: 'monospace'; font-size: 13px;">
<span style="color: #00FFC8;">🎨 SKIN HEX:</span>
<span style="background: #222; padding: 2px 8px; border-radius: 4px; color: #eee; border: 1px solid #444;">{hex_skin}</span>
<div style="width: 14px; height: 14px; background-color: {cor_preview}; border-radius: 50%; border: 1px solid #fff;"></div>
</div>
<div style="font-size: 10px; color: #555; margin-top: 15px; border-top: 1px solid #333; padding-top: 8px; text-align: right;">📅 ATUALIZADO EM: {data_att}</div>
</div>
""", unsafe_allow_html=True)
