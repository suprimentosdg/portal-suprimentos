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
st.markdown("Bem vindo ao portal de Gestão e controles administrativos do Setor de :blue[Suprimentos!]")
st.markdown("Escolha no Menu ao lado a opção desejada.")