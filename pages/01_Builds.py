import streamlit as st
from database import BUILDS_DB, PERKS_DB
from styles import apply_styles
import base64
import os

# --- CONFIGURAÇÃO DE CORES ORIGINAIS ---
COR_TITULO_PRINCIPAL = "#00ffcc"
COR_SET_EQUIPADO = "#ffffff"
COR_PERFORMANCE = "#ffffff"
COR_TEXTO_STATS = "#ffffff"
COR_BARRA_PROGRESSO = "#1afb02"  # Verde Neon
COR_LABEL_ROXO = "#bf00ff"       # Magenta para o Showcase

st.set_page_config(page_title="BR//WZ - Builds", layout="wide")
apply_styles()

# --- FUNÇÕES DE SUPORTE ---


def get_image_base64(path):
    if not path or not isinstance(path, str):
        return ""
    if path.startswith("http"):
        return path
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
    return ""


def render_perks(lista_perks, categoria):
    """Renderiza os blocos de Perks removendo quebras de linha para evitar erro de string."""
    html_total = ""
    for i, nome in enumerate(lista_perks):
        p = PERKS_DB.get(categoria, {}).get(
            nome, {"d": "Sem descrição", "v": "0%"})
        cor_titulo = "#ffd700" if i == 2 else "#ffffff"
        cor_desc = "#ffd700" if i == 2 else "#bbbbbb"

        # Montamos o bloco em uma string limpa
        bloco = f"""<div title="{p['d']}" style="background:rgba(0,0,0,0.2); border-radius:8px; padding:10px; margin-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05); cursor:help;"><div style="font-size:10px; color:#aaa; display:flex; justify-content:space-between; margin-bottom:2px;"><span>PERK {i+1}</span><span style="color:#ff8c00; font-weight:bold;">{p['v']}</span></div><div style="font-size:15px; font-weight:bold; color:{cor_titulo}; text-transform:uppercase;">{nome}</div><div style="font-size:10px; color:{cor_desc}; line-height:1.2; margin-top:4px; opacity:0.8; font-style:italic;">{p['d']}</div></div>"""

        html_total += bloco

    # Remove qualquer quebra de linha residual para o Streamlit não converter em texto
    return html_total.replace("\n", "")


# --- INTERFACE ---
if st.button("⬅️ VOLTAR AO MENU PRINCIPAL"):
    st.switch_page("home.py")

st.markdown(
    f'<h1 style="text-align: center; color: {COR_TITULO_PRINCIPAL}; text-shadow: 0 0 15px {COR_TITULO_PRINCIPAL}66; font-weight: 900; letter-spacing: 5px; margin-bottom: 30px;">CENTRAL DE BUILDS</h1>', unsafe_allow_html=True)

# Inicialização de states
if 'build_tipo' not in st.session_state:
    st.session_state.build_tipo = "FULL DPS"
if 'classe_build_selecionada' not in st.session_state:
    st.session_state.classe_build_selecionada = None

# --- NÍVEL 1: CATEGORIAS (COM CHECK ✅) ---
cats = list(BUILDS_DB.keys())
c_cols = st.columns(len(cats) + 2)
for i, cat in enumerate(cats):
    with c_cols[i]:
        is_active = (st.session_state.build_tipo == cat)
        label_botao = f"✅ {cat}" if is_active else cat
        if st.button(label_botao, key=f"bt_{cat}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.build_tipo = cat
            st.session_state.classe_build_selecionada = None
            st.rerun()

st.divider()

# --- NÍVEL 2: CLASSES (COM CHECK ✅) ---
b_data = BUILDS_DB.get(st.session_state.build_tipo)
if b_data:
    rec = b_data.get("classes_recomendadas", [])
    cl_cols = st.columns(len(rec) + 1)
    for i, cl in enumerate(rec):
        with cl_cols[i]:
            is_sel = (st.session_state.classe_build_selecionada == cl)
            label_classe = f"✅ {cl.upper()}" if is_sel else cl.upper()
            if st.button(label_classe, key=f"bcl_{cl}", use_container_width=True, type="primary" if is_sel else "secondary"):
                st.session_state.classe_build_selecionada = cl
                st.rerun()

    if st.session_state.classe_build_selecionada:
        classe_atual = st.session_state.classe_build_selecionada
        info_classe = b_data.get("detalhes_classes", {}).get(classe_atual, {})
        st.divider()

        # TAGS DE ESTILO
        tags = info_classe.get("tags", [])
        tag_html = "".join(
            [f'<span style="background:rgba(0, 255, 204, 0.1); border: 1px solid {COR_TITULO_PRINCIPAL}; color:{COR_TITULO_PRINCIPAL}; padding:3px 12px; border-radius:15px; font-size:10px; margin-right:8px; text-transform:uppercase; font-weight:bold;">{t}</span>' for t in tags])
        st.markdown(
            f'<div style="margin-bottom:25px;">{tag_html}</div>', unsafe_allow_html=True)

        cm, cs = st.columns([3, 1])

        with cm:
            st.markdown(
                f'<h3 style="color: {COR_SET_EQUIPADO}; margin-bottom: 25px;">🛡️ Build Sugerida: {classe_atual}</h3>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)

            with c1:
                for w in b_data.get("weapons", {}).get(classe_atual, []):
                    img = get_image_base64(w.get("img"))
                    cor_borda = "#4b99ff" if "escudo" in w['tipo'].lower(
                    ) else "#ff4b4b"
                    p_html = render_perks(w["perks"], "Weapon")
                    st.markdown(
                        f'<div class="build-card-container" style="border-left: 4px solid {cor_borda}; margin-bottom: 20px;"><div style="font-size:9px; color:{cor_borda}; font-weight:bold; margin-bottom:5px;">{w["tipo"].upper()}</div><div style="display:flex; align-items:center; margin-bottom:15px;"><div style="background:rgba(255,255,255,0.05); padding:5px; border-radius:8px; margin-right:12px;"><img src="{img}" style="width:42px; height:42px; object-fit:contain;"></div><div><b>{w["nome"]}</b><br><small style="color:#00ffff;">{w.get("stars")}</small></div></div>{p_html}</div>', unsafe_allow_html=True)

            with c2:
                arm = b_data.get("armor", {})
                p_html = render_perks(arm["perks"], "Armor")
                st.markdown(
                    f'<div class="build-card-container" style="border-left: 4px solid #00ffcc;"><div style="font-size:9px; color:#00ffcc; font-weight:bold; margin-bottom:5px;">ARMADURA</div><div style="display:flex; align-items:center; margin-bottom:15px;"><div style="background:rgba(255,255,255,0.05); padding:5px; border-radius:8px; margin-right:12px;"><img src="{get_image_base64(arm.get("img"))}" style="width:42px; height:42px; object-fit:contain;"></div><div><b>{arm["nome"]}</b></div></div>{p_html}</div>', unsafe_allow_html=True)

            with c3:
                pt = b_data.get("pet", {})
                p_html = render_perks(pt["perks"], "Pet")
                st.markdown(
                    f'<div class="build-card-container" style="border-left: 4px solid #ffcc00;"><div style="font-size:9px; color:#ffcc00; font-weight:bold; margin-bottom:5px;">COMPANION</div><div style="display:flex; align-items:center; margin-bottom:15px;"><div style="background:rgba(255,255,255,0.05); padding:5px; border-radius:8px; margin-right:12px;"><img src="{get_image_base64(pt.get("img"))}" style="width:42px; height:42px; object-fit:contain;"></div><div><b>{pt["nome"]}</b></div></div>{p_html}</div>', unsafe_allow_html=True)

        with cs:
            st.markdown(
                f'<h3 style="color: {COR_PERFORMANCE}; margin-bottom: 20px;">📊 Stats</h3>', unsafe_allow_html=True)
            st.markdown(
                f"""<style>.stProgress > div > div > div > div {{ background-color: {COR_BARRA_PROGRESSO} !important; box-shadow: 0 0 15px {COR_BARRA_PROGRESSO}aa; }}</style>""", unsafe_allow_html=True)
            for s, v in b_data.get("stats", {}).items():
                st.markdown(
                    f'<p style="color: {COR_TEXTO_STATS}; font-weight: bold; margin-bottom: -15px; font-size: 14px;">{s.upper()}</p>', unsafe_allow_html=True)
                st.progress(v/100)

        # --- GUIA DE COMBATE ---
        dica = info_classe.get("dica")
        if dica:
            st.markdown(f"""<div style="background: rgba(26, 251, 2, 0.03); border-left: 5px solid {COR_BARRA_PROGRESSO}; padding: 25px; border-radius: 0 12px 12px 0; margin-top: 40px; border-top: 1px solid rgba(255,255,255,0.05);"><div style="color: {COR_BARRA_PROGRESSO}; font-weight: bold; font-size: 15px; margin-bottom: 10px; display: flex; align-items: center;"><span style="margin-right:12px; font-size: 20px;">💡</span> GUIA DE COMBATE - {classe_atual.upper()}</div><div style="color: #ddd; font-size: 14px; line-height: 1.6; font-style: italic;">"{dica}"</div></div>""", unsafe_allow_html=True)

        # --- SHOWCASE SKILLS (ABAIXO DO GUIA) ---
        url_video = info_classe.get("video")
        if url_video:
            st.markdown(f"""<div style="background: rgba(191, 0, 255, 0.03); border-left: 5px solid {COR_LABEL_ROXO}; padding: 25px; border-radius: 0 12px 12px 0; margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.05);"><div style="color: {COR_LABEL_ROXO}; font-weight: bold; font-size: 15px; margin-bottom: 20px; display: flex; align-items: center; letter-spacing: 1px;"><span style="margin-right:12px; font-size: 20px;">📺</span> SHOWCASE DE SKILLS - {classe_atual.upper()}</div></div>""", unsafe_allow_html=True)
            v_col1, v_col2, v_col3 = st.columns([1, 6, 1])
            with v_col2:
                st.video(url_video)

# --- 5. ANÁLISE TÉCNICA (NOVO LABEL DE RESUMO) ---
        analise = info_classe.get("analise_tecnica")
        if analise:
            st.markdown(f"""
                <div style="background: rgba(0, 255, 204, 0.02); border-left: 5px solid {COR_TITULO_PRINCIPAL}; padding: 25px; border-radius: 0 12px 12px 0; margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.05);">
                    <div style="color: {COR_TITULO_PRINCIPAL}; font-weight: bold; font-size: 15px; margin-bottom: 10px; display: flex; align-items: center; letter-spacing: 1px;">
                        <span style="margin-right:12px; font-size: 20px;">🔬</span> ANÁLISE TÉCNICA DE EQUIPAMENTOS
                    </div>
                    <div style="color: #ccc; font-size: 13px; line-height: 1.8;">{analise}</div>
                </div>
            """, unsafe_allow_html=True)

        # --- 6. LABELS FINAIS: CRÉDITOS E PARCERIA ---
        st.markdown("<br>", unsafe_allow_html=True)
        footer_c1, footer_c2 = st.columns(2)
        
        with footer_c1:
            creditos = info_classe.get("creditos", "Equipe BR//WZ")
            st.markdown(f"""<div style="background: rgba(255, 255, 255, 0.03); border-left: 5px solid #00ffff; padding: 20px; border-radius: 0 10px 10px 0; border-top: 1px solid rgba(255,255,255,0.05);"><div style="color: #00ffff; font-weight: bold; font-size: 13px; margin-bottom: 5px;">🤝 CRÉDITOS / COLABORAÇÃO</div><div style="color: #ccc; font-size: 12px;">{creditos}</div></div>""", unsafe_allow_html=True)
        
        with footer_c2:
            parceria = info_classe.get("parceria", "Espaço para Parceiros")
            st.markdown(f"""<div style="background: rgba(255, 255, 255, 0.03); border-left: 5px solid #ffd700; padding: 20px; border-radius: 0 10px 10px 0; border-top: 1px solid rgba(255,255,255,0.05);"><div style="color: #ffd700; font-weight: bold; font-size: 13px; margin-bottom: 5px;">⭐ PARCERIA / APOIO</div><div style="color: #ccc; font-size: 12px;">{parceria}</div></div>""", unsafe_allow_html=True)
