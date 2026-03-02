import streamlit as st
import json
import os
# Importamos a alma visual do site para garantir a simetria
from interface import aplicar_estilo, exibir_cabecalho, exibir_nav

# 1. Configuração da Página
st.set_page_config(page_title="Tutoriais - W//Z Wiki",
                   layout="wide", page_icon="📖")

# 2. Carregar Dados


def carregar_dados():
    if not os.path.exists('database.json'):
        return {"home": {}, "builds": [], "pets": []}
    with open('database.json', 'r', encoding='utf-8') as f:
        return json.load(f)


dados = carregar_dados()

# --- APLICANDO A INTERFACE PADRONIZADA ---
aplicar_estilo()        # Carrega o CSS global
exibir_cabecalho(dados)  # Gera Título e Stats
exibir_nav("TUTORIAIS")  # Gera o Menu (Marcando 'TUTORIAIS' como ativo)

# --- CONTEÚDO ESPECÍFICO (AVISO DE CONSTRUÇÃO) ---
st.write("")
st.write("")

# Usando um container estilizado para o aviso
st.markdown("""
    <div style="
        text-align: center; 
        padding: 80px 20px; 
        background: rgba(255, 255, 255, 0.02); 
        border: 1px dashed #4a3f10; 
        border-radius: 15px;
        margin: 20px 0;
    ">
        <h1 style="color: #f1c40f; font-size: 50px; margin-bottom: 10px;">🚧</h1>
        <h2 style="color: #f1c40f; font-family: 'Rajdhani'; text-transform: uppercase; letter-spacing: 3px;">Página em Construção</h2>
        <p style="color: #888; font-size: 16px;">Estamos preparando os melhores guias e tutoriais para a comunidade brasileira.</p>
        <p style="color: #4a3f10; font-size: 12px; margin-top: 20px;">DISPONÍVEL EM BREVE</p>
    </div>
""", unsafe_allow_html=True)

# Rodapé simples
st.write("---")
st.caption("W//Z Wiki - Comunidade Brasileira")
