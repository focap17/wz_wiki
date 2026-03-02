import streamlit as st
import json
import os
from datetime import datetime

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Admin W//Z - Controle Total", layout="wide")


def carregar_dados():
    if not os.path.exists('database.json'):
        return {
            "home": {"ultima_atualizacao": "", "noticias": [], "evento_ativo": {}, "status_server": "ONLINE", "codigos_ativos": "", "bem_vindo": ""},
            "builds": [],
            "pets": [],
            "marketplace": [],
            "perks_disponiveis": {"arma": [], "armadura": [], "pet": []}
        }
    with open('database.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
        if "perks_disponiveis" not in dados:
            dados["perks_disponiveis"] = {
                "arma": [], "armadura": [], "pet": []}
        if "pets" not in dados:
            dados["pets"] = []
        if "marketplace" not in dados:
            dados["marketplace"] = []
        return dados


def salvar_dados(dados):
    with open('database.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


dados = carregar_dados()

lista_todas_classes = sorted([
    "Espadachim", "Paladino", "Dualwilder", "Elementalist", "Guardian", "Mage of Light",
    "Berserker", "Spirit Archer", "Demon", "Dragoon", "Warlord",
    "Summoner", "Shadowhunter", "Hunter", "Leviathan", "Starbreaker",
    "Necromancer", "Stormcaller", "Shadowmage"
])

# --- LOGIN ---
senha = st.sidebar.text_input("Chave de Acesso", type="password")

if senha == "1234":
    st.title("⚙️ Painel de Gestão Wiki")
    tabs = st.tabs(["🛡️ Gerenciar Builds", "🐾 Pets",
                   "✨ Banco de Perks", "📰 Notícias", "🌐 Home", "🛒 Market"])

    # --- ABA 0: GERENCIAR BUILDS ---
    with tabs[0]:
        st.subheader("🛡️ Nova Build")
        usar_duas_armas = st.toggle(
            "⚔️ Habilitar Segunda Arma (Dual Slot)", value=False)
        perks_arma = sorted(dados["perks_disponiveis"]["arma"])
        perks_armor = sorted(dados["perks_disponiveis"]["armadura"])
        perks_pet = sorted(dados["perks_disponiveis"]["pet"])

        with st.form("build_form_v4", clear_on_submit=True):
            c1, c2 = st.columns(2)
            b_nome = c1.text_input("Nome da Build")
            b_autor = c2.text_input("Autor")
            c3, c4 = st.columns(2)
            b_classe = c3.selectbox("Classe", lista_todas_classes)
            b_kit = c4.text_input("Kit (ex: 2x Longsword)")
            b_tags = st.multiselect("Tags da Build", [
                                    "DPS", "Tank", "Suporte", "Eventos", "SpeedFarm"])
            st.write("---")
            build_perks = {"armas": [], "armadura": [], "pet": []}
            st.markdown("### ⚔️ ARMA 1")
            col_w1 = st.columns(3)
            w1p1 = col_w1[0].selectbox(
                "Perk 1 - Arma 1", ["-"] + perks_arma, key="nw1p1")
            w1p2 = col_w1[1].selectbox(
                "Perk 2 - Arma 1", ["-"] + perks_arma, key="nw1p2")
            w1p3 = col_w1[2].selectbox(
                "Perk 3 - Arma 1", ["-"] + perks_arma, key="nw1p3")
            build_perks["armas"].append([w1p1, w1p2, w1p3])

            if usar_duas_armas:
                st.markdown("### ⚔️ ARMA 2")
                col_w2 = st.columns(3)
                w2p1 = col_w2[0].selectbox(
                    "Perk 1 - Arma 2", ["-"] + perks_arma, key="nw2p1")
                w2p2 = col_w2[1].selectbox(
                    "Perk 2 - Arma 2", ["-"] + perks_arma, key="nw2p2")
                w2p3 = col_w2[2].selectbox(
                    "Perk 3 - Arma 2", ["-"] + perks_arma, key="nw2p3")
                build_perks["armas"].append([w2p1, w2p2, w2p3])

            st.write("---")
            col_ap = st.columns(2)
            with col_ap[0]:
                st.markdown("### 🛡️ ARMADURA")
                ar1 = st.selectbox(
                    "Perk 1 Armor", ["-"] + perks_armor, key="nar1")
                ar2 = st.selectbox(
                    "Perk 2 Armor", ["-"] + perks_armor, key="nar2")
                ar3 = st.selectbox(
                    "Perk 3 Armor", ["-"] + perks_armor, key="nar3")
                build_perks["armadura"] = [ar1, ar2, ar3]
            with col_ap[1]:
                st.markdown("### 🐾 PET")
                pt1 = st.selectbox("Perk 1 Pet", ["-"] + perks_pet, key="npt1")
                pt2 = st.selectbox("Perk 2 Pet", ["-"] + perks_pet, key="npt2")
                pt3 = st.selectbox("Perk 3 Pet", ["-"] + perks_pet, key="npt3")
                build_perks["pet"] = [pt1, pt2, pt3]

            b_video = st.text_input("Link YouTube")
            b_desc = st.text_area("Descrição / Notas de Uso")

            if st.form_submit_button("🚀 PUBLICAR BUILD"):
                nova = {"nome": b_nome, "autor": b_autor, "classe": b_classe, "kit": b_kit, "tags": b_tags, "usa_duas_armas": usar_duas_armas,
                        "perks": build_perks, "video": b_video, "desc": b_desc, "data": datetime.now().strftime("%d/%m/%Y")}
                dados["builds"].insert(0, nova)
                salvar_dados(dados)
                st.success("Build Publicada!")
                st.rerun()

        # --- AQUI ESTAVA O ERRO: FALTAVA ESTA SEÇÃO ABAIXO ---
        st.write("---")
        st.subheader("🛡️ Builds Publicadas")

        builds_cadastradas = dados.get("builds", [])
        if not builds_cadastradas:
            st.info("Nenhuma build encontrada.")
        else:
            for i, b in enumerate(builds_cadastradas):
                with st.expander(f"📌 {b.get('classe')} - {b.get('nome')} (por {b.get('autor')})"):
                    col_b1, col_b2 = st.columns([4, 1])
                    col_b1.write(
                        f"**Data:** {b.get('data')} | **Tags:** {', '.join(b.get('tags', []))}")
                    if col_b2.button("🗑️ Excluir Build", key=f"del_build_{i}"):
                        dados["builds"].pop(i)
                        salvar_dados(dados)
                        st.rerun()

    with tabs[1]:
        st.subheader("🐾 Banco de Dados de Pets")
        with st.form("form_pet_new", clear_on_submit=True):
            c1, c2 = st.columns(2)
            p_nome = c1.text_input("Nome do Pet")
            p_obtencao = c2.text_input("Obtenção (Ex: Mundo 4)")
            c3, c4 = st.columns(2)
            p_skill_nome = c3.text_input("Nome da Skill")
            p_elemento = c4.selectbox("Elemento", [
                                      "🔥 Fogo", "❄️ Gelo", "⚡ Raio", "🌿 Planta", "✨ Luz", "🌑 Trevas", "💧 Água", "🛡️ Defesa", "❤️ Cura"])
            p_tags_skill = st.multiselect(
                "Mecânicas", ["Single Target", "AoE", "DoT", "Buff", "Debuff", "Stun", "Passive"])
            p_skill_desc = st.text_area("Descrição da Skill")
            if st.form_submit_button("✅ Cadastrar Pet"):
                dados["pets"].insert(0, {"nome": p_nome, "obtencao": p_obtencao, "skill_nome": p_skill_nome,
                                     "elemento": p_elemento, "tags_skill": p_tags_skill, "skill_desc": p_skill_desc})
                salvar_dados(dados)
                st.success("Pet cadastrado!")
                st.rerun()
        for i, p in enumerate(dados.get("pets", [])):
            with st.expander(f"🐾 {p.get('elemento')} - {p['nome']}"):
                if st.button(f"🗑️ Excluir {p['nome']}", key=f"del_p_{i}"):
                    dados["pets"].pop(i)
                    salvar_dados(dados)
                    st.rerun()

    with tabs[2]:
        st.subheader("✨ Banco de Perks")
        with st.form("perk_form"):
            c1, c2 = st.columns(2)
            np_nome = c1.text_input("Nome do Perk")
            np_tipo = c2.selectbox("Tipo", ["arma", "armadura", "pet"])
            if st.form_submit_button("Adicionar"):
                if np_nome not in dados["perks_disponiveis"][np_tipo]:
                    dados["perks_disponiveis"][np_tipo].append(np_nome)
                    salvar_dados(dados)
                    st.rerun()
        col_p1, col_p2, col_p3 = st.columns(3)
        for t, c in zip(["arma", "armadura", "pet"], [col_p1, col_p2, col_p3]):
            c.markdown(f"### **{t.upper()}**")
            for p in sorted(dados["perks_disponiveis"][t]):
                if c.button(f"🗑️ {p}", key=f"d_{t}_{p}"):
                    dados["perks_disponiveis"][t].remove(p)
                    salvar_dados(dados)
                    st.rerun()

    with tabs[3]:
        st.subheader("📰 Gerenciar Notícias")
        if "noticias" not in dados:
            dados["noticias"] = []
        with st.form("news_f", clear_on_submit=True):
            titulo_n = st.text_input("Título da Notícia")
            conteudo_n = st.text_area(
                "Conteúdo (Use Enter para pular linhas)", height=200)
            if st.form_submit_button("🚀 Postar Notícia"):
                if titulo_n and conteudo_n:
                    nova_noticia = {"titulo": titulo_n, "conteudo": conteudo_n,
                                    "data": datetime.now().strftime("%d/%m/%Y %H:%M")}
                    dados["noticias"].insert(0, nova_noticia)
                    salvar_dados(dados)
                    st.success("Notícia publicada!")
                    st.rerun()
        for i, n in enumerate(dados.get("noticias", [])):
            col_del_1, col_del_2 = st.columns([4, 1])
            col_del_1.write(f"**{n.get('titulo')}** ({n.get('data')})")
            if col_del_2.button("Excluir", key=f"del_not_{i}"):
                dados["noticias"].pop(i)
                salvar_dados(dados)
                st.rerun()

    with tabs[4]:
        st.subheader("🌐 Configurações da Home")
        with st.form("form_home_config"):
            status_atual = dados["home"].get("status_server", "ONLINE")
            novo_status = st.radio("Status Global:", [
                                   "ONLINE", "MANUTENÇÃO"], index=0 if status_atual == "ONLINE" else 1)
            ev = dados["home"].get("evento_ativo", {})
            titulo_ev = st.text_input("Evento", value=ev.get("titulo", ""))
            desc_ev = st.text_area("Descrição do Evento",
                                   value=ev.get("descricao", ""))
            data_ev = st.text_input(
                "Término (Ex: 06/03)", value=ev.get("termina_em", ""))
            novos_codigos = st.text_area(
                "Códigos Ativos (Um por linha)", value=dados["home"].get("codigos_ativos", ""))
            msg_welcome = st.text_area(
                "Texto de Boas-Vindas", value=dados["home"].get("bem_vindo", "Bem-vindo à nossa Wiki!"))
            if st.form_submit_button("💾 Salvar Alterações"):
                dados["home"].update({"status_server": novo_status, "evento_ativo": {"titulo": titulo_ev, "descricao": desc_ev, "termina_em": data_ev},
                                     "codigos_ativos": novos_codigos, "bem_vindo": msg_welcome, "ultima_atualizacao": datetime.now().strftime("%d/%m/%Y")})
                salvar_dados(dados)
                st.success("Home atualizada!")
                st.rerun()

    # --- ABA 5: MARKETPLACE (GUIA DE PREÇOS) ---
    with tabs[5]:
        st.subheader("🛒 Gerenciar Guia de Preços")

        with st.form("form_market", clear_on_submit=True):
            col1, col2 = st.columns(2)
            item_nome = col1.text_input("Nome do Item")
            item_cat = col2.selectbox(
                "Categoria", ["Aura", "Weapon Skin", "Hat", "Tail", "Back", "Costume", "Mount", "Both", "Furniture"])

            col3, col4 = st.columns(2)
            item_preco = col3.number_input(
                "Preço (Gold)", min_value=0, step=1000)
            # AQUI: Inserção do Hex como texto informativo
            item_hex = col4.text_input(
                "Hex", placeholder="Ex: #FFFFFF")

            if st.form_submit_button("✅ Adicionar"):
                if item_nome:
                    novo_item = {
                        "nome": item_nome,
                        "categoria": item_cat,
                        "preco": item_preco,
                        "hex_original": item_hex,  # Salva como texto normal
                        "atualizado_em": datetime.now().strftime("%d/%m/%Y")
                    }
                    dados["marketplace"].insert(0, novo_item)
                    salvar_dados(dados)
                    st.success(f"{item_nome} adicionado!")
                    st.rerun()
                else:
                    st.error("O nome é obrigatório.")

        st.write("---")
        st.subheader("📦 Itens Cadastrados")
        for i, item in enumerate(dados.get("marketplace", [])):
            col_i1, col_i2, col_i3, col_i4 = st.columns([3, 2, 2, 1])
            col_i1.write(f"**{item['nome']}**")
            col_i2.write(f"💰 {item['preco']:,}")
            col_i3.write(f"🎨 HEX: `{item.get('hex_original', 'N/A')}`")
            if col_i4.button("🗑️", key=f"del_m_{i}"):
                dados["marketplace"].pop(i)
                salvar_dados(dados)
                st.rerun()
else:
    st.info("Aguardando senha...")
