import streamlit as st
from styles import apply_styles

# 1. Configurações Iniciais da Página
st.set_page_config(
    page_title="BR//WZ - A WIKI DEFINITIVA!",
    layout="wide",
    page_icon="⚔️",
    initial_sidebar_state="collapsed"
)

# Aplicando os estilos CSS do seu arquivo styles.py
apply_styles()

# 2. Cabeçalho Principal
# Espaçamento para centralizar verticalmente um pouco mais
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<p class="neon-title">BR//WZ - A WIKI DEFINITIVA!</p>',
            unsafe_allow_html=True)
st.markdown('<p class="subtitle">DATABASE WIKI DEDICADA A COMUNIDADE BRASILEIRA DO WORLD//ZERO</p>',
            unsafe_allow_html=True)

# 3. Menu de Navegação (Botões Principais)
# Usamos colunas vazias nas pontas para manter os botões agrupados no centro
_, col_menu, _ = st.columns([1, 10, 1])

with col_menu:
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("🛡️\nBUILDS", use_container_width=True):
            st.switch_page("pages/01_Builds.py")
    with c2:
        if st.button("⚔️\nCLASSES", use_container_width=True):
            st.switch_page("pages/02_Classes.py")
    with c3:
        if st.button("🐾\nPETS", use_container_width=True):
            st.switch_page("pages/03_Pets.py")
    with c4:
        if st.button("🗺️\nMUNDOS", use_container_width=True):
            st.switch_page("pages/04_Mundos.py")

# Divisor Estético
st.markdown("<br><hr style='border: 0.5px solid #333; opacity: 0.2;'><br>",
            unsafe_allow_html=True)

# 4. Dashboard Inferior (Informações e Comunidade)
col_build, col_eventos, col_social = st.columns([1.2, 1, 1])

# --- Coluna 1: Build da Semana ---
with col_build:
    st.markdown("### 🏆 Build da Semana")
    st.markdown("""
        <div style="background: rgba(0, 255, 204, 0.05); padding: 20px; border-radius: 15px; border: 1px solid #00ffcc; min-height: 200px;">
            <p style="color: #00ffcc; font-weight: bold; font-size: 11px; letter-spacing: 1px; margin-bottom: 5px;">DESTAQUE ATUAL</p>
            <h4 style="margin: 0; color: white; font-size: 22px;">Berserker "God Slayer"</h4>
            <p style="font-size: 14px; color: #bbb; margin: 15px 0;">Focada em regeneração de vida por acerto e dano crítico massivo para sololar o Mundo 6.</p>
            <div style="display: flex; gap: 10px;">
                <span style="background: rgba(0,255,204,0.2); color: #00ffcc; padding: 2px 8px; border-radius: 4px; font-size: 10px;">TIER S+</span>
                <span style="background: rgba(255,255,255,0.1); color: white; padding: 2px 8px; border-radius: 4px; font-size: 10px;">LIFESTEAL</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Explorar Builds ➔", key="go_builds"):
        st.switch_page("pages/01_Builds.py")

# --- Coluna 2: Eventos Disponíveis ---
with col_eventos:
    st.markdown("### 📅 Eventos")
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.02); padding: 18px; border-radius: 15px; border: 1px solid #333; min-height: 200px;">
            <div style="margin-bottom: 20px;">
                <span style="background: green; color: white; padding: 3px 10px; border-radius: 5px; font-size: 10px; font-weight: bold;">ATIVO</span>
                <p style="margin: 8px 0 0 0; font-size: 15px; font-weight: bold; color: #eee;">Evento Cupid Boss</p>
                <p style="color: #666; font-size: 12px; margin: 0;">Derrote o Cupid e tenha acesso a várias recompensas!</p>
            </div>
            <div style="margin-bottom: 5px; opacity: 0.7;">
                <span style="background: red; color: white; padding: 3px 10px; border-radius: 5px; font-size: 10px; font-weight: bold;">EM BREVE</span>
                <p style="margin: 8px 0 0 0; font-size: 15px; font-weight: bold; color: #eee;">Próximo Passe de Batalha</p>
                <p style="color: #666; font-size: 12px; margin: 0;">Início: 01 de Março</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- Coluna 3: Contato, Discord e Parceria ---
with col_social:
    st.markdown("### 🤝 Comunidade BR//WZ")

    # Label Discord
    st.markdown("""
        <div style="background: #5865F2; padding: 12px; border-radius: 12px; margin-bottom: 12px; display: flex; align-items: center; gap: 15px; border: 1px solid rgba(255,255,255,0.1);">
            <span style="font-size: 24px;">💬</span>
            <div style="line-height: 1.1;">
                <b style="font-size: 14px; color: white;">DISCORD OFICIAL</b><br>
                <a href="#" style="color: rgba(255,255,255,0.7); font-size: 11px; text-decoration: none;">Comunidade e Suporte</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Label Parceria
    st.markdown("""
        <div style="background: rgba(255,204,0,0.05); padding: 12px; border-radius: 12px; margin-bottom: 12px; border: 1px dashed #ffcc00;">
            <b style="font-size: 13px; color: #ffcc00;">✨ PARCERIA</b><br>
            <p style="font-size: 11px; color: #888; margin: 4px 0 0 0;">Anuncie sua Guilda ou Loja aqui.</p>
        </div>
    """, unsafe_allow_html=True)

    # Label Contato
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.05); padding: 12px; border-radius: 12px;">
            <b style="font-size: 13px; color: #00ffcc;">✉️ CONTATO</b><br>
            <p style="font-size: 11px; color: #bbb; margin: 4px 0 0 0;">Dúvidas ou Sugestões:<br><b>email@embreve</b></p>
        </div>
    """, unsafe_allow_html=True)

# 5. Rodapé Final
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; font-size:11px; letter-spacing: 2px;'>WORLD ZERO DATABASE PROJECT © 2026</p>", unsafe_allow_html=True)
