import streamlit as st
import numpy as np
from datetime import datetime
import pandas as pd
from pymongo import MongoClient

st.set_page_config(page_title="Portal de Suprimentos")
col1, col2 = st.columns([4, 1])
col1.title("Portal de Suprimentos")
image_path = "logo_globo.png"
image = col2.image(image_path, width=80)
st.subheader("Página inicial")
st.write("---")
st.markdown("Bem vindo ao portal do Setor de :blue[Suprimentos!]")
st.markdown("O Portal de Suprimentos é uma plataforma online que facilita a o gerenciamento das compras e de seus processos que estão sob responsabilidade do Suprimentos. Aqui você pode:")
st.write(
    "- Confirmar as entregas dos seus pedidos de forma rápida e segura;"
    "- Abrir chamados para solicitar manutenção, troca de impressoras e solicitações de toner;"
    "- Consultar os produtos disponíveis para solicitação de sua loja, junto com os códigos deles;"
    "- Entrar em contato com o setor, que está sempre pronto para te atender e resolver qualquer problema.")
st.markdown("Escolha no Menu ao lado a opção desejada.")