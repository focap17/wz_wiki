import streamlit as st
from styles import apply_styles
from data.noticias import NEWS_LIST

st.set_page_config(page_title="Notícias - World Zero", layout="wide")
apply_styles()

st.markdown("## 📰 Histórico de Atualizações")

for news in NEWS_LIST:
    with st.container():
        st.markdown(f"### {news['titulo']}")
        st.caption(f"📅 {news['data']} | 🏷️ {news['tag']}")
        st.write(news['corpo'])
        st.markdown("---")
