import streamlit as st
import json
import os
# Importamos a alma visual do site para garantir a simetria total
from interface import aplicar_estilo, exibir_cabecalho, exibir_nav

# 1. Configuração da Página
st.set_page_config(page_title="Discord - W//Z Wiki",
                   layout="wide", page_icon="💬")

# 2. Carregar Dados


def carregar_dados():
    if not os.path.exists('database.json'):
        return {"home": {}, "builds": [], "pets": []}
    with open('database.json', 'r', encoding='utf-8') as f:
        return json.load(f)


dados = carregar_dados()

# --- APLICANDO A INTERFACE PADRONIZADA ---
aplicar_estilo()        # Carrega o CSS global do interface.py
exibir_cabecalho(dados)  # Gera Título e Stats
exibir_nav("DISCORD")   # Gera o Menu (Marcando 'DISCORD' como ativo)

# --- CONTEÚDO ESPECÍFICO (AVISO DE CONSTRUÇÃO DO DISCORD) ---
st.write("")
st.write("")

# Container estilizado com o sublinhado traçado (border: dashed)
st.markdown("""
    <div style="
        text-align: center; 
        padding: 80px 20px; 
        background: rgba(255, 255, 255, 0.02); 
        border: 1px dashed #4a3f10; 
        border-radius: 15px;
        margin: 20px 0;
    ">
        <h1 style="color: #5865F2; font-size: 50px; margin-bottom: 10px;">💬</h1>
        <h2 style="color: #f1c40f; font-family: 'Rajdhani'; text-transform: uppercase; letter-spacing: 3px;">Comunidade no Discord</h2>
        <p style="color: #888; font-size: 16px;">Estamos configurando o servidor oficial da comunidade brasileira para receber todos os jogadores.</p>
        
        <div style="margin-top: 30px; padding: 10px; border-top: 1px dashed #4a3f10; display: inline-block; width: 60%;">
            <p style="color: #4a3f10; font-size: 12px; font-weight: bold; text-transform: uppercase;">
                Convites Liberados em Breve
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Rodapé simples
st.write("---")
st.caption("W//Z Wiki - Sincronizado via Discord Hub")
