import streamlit as st
import json


def carregar_dados():
    with open('database.json', 'r', encoding='utf-8') as f:
        return json.load(f)


st.title("🛡️ Classes do Jogo")

dados = carregar_dados()
classes = dados['classes']

# Selecionar a classe para ver detalhes
classe_selecionada = st.selectbox("Escolha uma classe:", list(classes.keys()))

if classe_selecionada:
    info = classes[classe_selecionada]
    st.subheader(f"Classe: {classe_selecionada}")
    st.markdown(f"**Tier:** {info['tier']}")
    st.write(info['descricao'])

    st.write("---")
    st.subheader("Habilidades:")
    for hab in info['habilidades']:
        st.write(f"- {hab}")
