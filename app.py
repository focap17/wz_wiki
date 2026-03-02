import streamlit as st
import json
import os
from interface import aplicar_estilo, exibir_cabecalho, exibir_nav

# 1. Configuração da Página
st.set_page_config(page_title="W//Z Wiki - Home",
                   layout="wide", page_icon="🛡️")

# 2. Carregar Dados


def carregar_dados():
    if not os.path.exists('database.json'):
        return {"home": {}, "noticias": [], "builds": []}
    with open('database.json', 'r', encoding='utf-8') as f:
        return json.load(f)


dados = carregar_dados()

# --- APLICANDO A INTERFACE PADRONIZADA ---
aplicar_estilo()
exibir_cabecalho(dados)
exibir_nav("INÍCIO")

# --- LAYOUT DA HOME ---
col_noticias, col_info = st.columns([2, 1])

# --- COLUNA DA ESQUERDA: NOTÍCIAS (LIMITADO ÀS 3 MAIS RECENTES) ---
with col_noticias:
    st.markdown('<h2 style="font-family: \'Rajdhani\'; color: #f1c40f; letter-spacing: 2px;">📰 ÚLTIMAS NOTÍCIAS</h2>', unsafe_allow_html=True)

    # Pegamos as notícias do banco de dados (raiz do JSON)
    lista_noticias = dados.get("noticias", [])

    if not lista_noticias:
        st.info("Nenhuma notícia disponível no momento.")
    else:
        # Exibe apenas as 3 mais recentes para não poluir a Home
        for noticia in lista_noticias[:3]:
            with st.container():
                st.markdown(f"""
                    <div class="content-card">
                        <div style="color: #666; font-size: 10px; margin-bottom: 5px; font-weight: bold;">
                            📅 {noticia.get('data', '00/00/2026')}
                        </div>
                        <h3 style="color: #f1c40f; margin-top: 0; font-family: 'Rajdhani'; letter-spacing: 1px;">
                            {noticia.get('titulo', 'SEM TÍTULO').upper()}
                        </h3>
                        <div style="
                            font-family: 'Rajdhani', sans-serif; 
                            font-size: 15px; 
                            line-height: 1.6; 
                            color: #e0e0e0;
                            white-space: pre-line; 
                        ">
                            {noticia.get('conteudo', '')}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        if len(lista_noticias) > 3:
            st.markdown(f'<p style="text-align:center; color:#555; font-size:12px; font-family: \'Rajdhani\';">Exibindo as 3 notícias mais recentes.</p>', unsafe_allow_html=True)

# --- COLUNA DA DIREITA: EVENTO > BOAS-VINDAS > LINKS > CÓDIGOS ---
with col_info:

    # 1. EVENTO ATIVO
    evento = dados["home"].get("evento_ativo", {})
    if evento and evento.get("titulo"):
        st.markdown(f"""
            <div class="content-card" style="border-left-color: #ff4b4b; background: rgba(255, 75, 75, 0.05);">
                <h3 style="color: #ff4b4b; font-family: 'Rajdhani'; margin-top: 0;">🔥 EVENTO ATIVO</h3>
                <p style="font-weight: bold; color: #fff; margin-bottom: 5px; font-family: 'Rajdhani';">{evento.get('titulo')}</p>
                <p style="font-size: 13px; color: #ccc; font-family: 'Rajdhani';">{evento.get('descricao')}</p>
                <div style="background: rgba(0,0,0,0.3); padding: 5px; border-radius: 4px; text-align: center; font-size: 11px; color: #ff4b4b; font-weight: bold; border: 1px solid #ff4b4b; font-family: 'Rajdhani';">
                    ⏳ TERMINA EM: {evento.get('termina_em')}
                </div>
            </div>
        """, unsafe_allow_html=True)

    # 2. BOAS-VINDAS
    st.markdown(f"""
        <div class="content-card">
            <h3 style="color: #f1c40f; font-family: 'Rajdhani'; margin-top: 0;">BOAS-VINDAS</h3>
            <div style="font-family: 'Rajdhani'; font-size: 14px; line-height: 1.5; color: #e0e0e0;">
                {dados['home'].get('bem_vindo', 'Bem-vindo à nossa Wiki oficial da comunidade brasileira!')}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. LINKS ÚTEIS
    st.markdown("""
        <div class="content-card" style="border-left-color: #00FFC8;">
            <h4 style="color: #00FFC8; font-family: 'Rajdhani'; margin-top: 0;">LINKS ÚTEIS</h4>
            <div style="font-family: 'Rajdhani'; font-size: 13px;">
                <p style="margin-bottom: 8px;">🔗 <a href="#" style="color: #ccc; text-decoration: none;">Wiki Global</a></p>
                <p>🔗 <a href="#" style="color: #ccc; text-decoration: none;">Discord da Guilda</a></p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. CÓDIGOS ATIVOS (Gerido pelo Painel Admin)
    codigos_at_txt = dados["home"].get(
        "codigos_ativos", "Nenhum código ativo no momento.")
    st.markdown(f"""
        <div class="content-card" style="border-left-color: #f1c40f; background: rgba(241, 196, 15, 0.05);">
            <h4 style="color: #f1c40f; font-family: 'Rajdhani'; margin-top: 0;">🎁 CÓDIGOS ATIVOS</h4>
            <div style="font-family: 'Rajdhani'; font-size: 14px; color: #fff; white-space: pre-line;">
                {codigos_at_txt}
            </div>
        </div>
    """, unsafe_allow_html=True)

# Divisor Final
st.markdown('<div class="divisor-tracejado"></div>', unsafe_allow_html=True)
