import streamlit as st
from datetime import datetime
from pymongo import MongoClient

connectString = "mongodb+srv://suprimentosdglobo:suprimentosdg2023@cluster0.dx7yrgp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connectString)
db = client["confirmations"]
mycolection = db.Cl01

st.set_page_config(page_title="Confirmação de Entrega")
col1, col2 = st.columns([4, 1])
col1.title("Portal de Suprimentos")
image_path = "logo_globo.png"
image = col2.image(image_path, width=80)
st.subheader("Confirmação de entregas")

regions = ["Piauí", "Maranhão", "Rio Grande do Norte", "Bahia", "Pará"]
suppliers = ["Atlas Papelaria", "Atakadinho Bahia", "Brilhante", "Casa Norte", "Distribuidora Teresina", "Ecopaper", "E Pacheco", "KC Carvalho", "Macropack", "Nacional", "PL", "Supermercado Jorge Batista"]

with st.form(key="include_confirmation"):
    name1 = st.text_input("Digite seu nome:", )
    region1 = st.selectbox("Selecione sua regional:", regions)
    store1 = st.number_input("Digite sua loja:", min_value=0, max_value=999)
    supplier = st.selectbox("Selecione o Fornecedor:", suppliers)
    date = st.date_input("Data do recebimento:", format="DD/MM/YYYY")
    nf = st.number_input("N° da Nota Fiscal:", step=1, format="%d")
    send1 = st.form_submit_button("Enviar")
    if send1:
        formatted_date = datetime.strftime(date, "%d/%m/%Y")
        current_timestamp = datetime.now().timestamp()
        formatted_timestamp = datetime.fromtimestamp(current_timestamp).strftime("%d/%m/%Y %H:%M:%S")

        if not name1 or not region1 or not store1 or not supplier or not date or not nf:
            st.warning("Por favor, preencha todos os campos.")
        else:
            data_to_insert = {
                'nome': name1,
                'regional': region1,
                'loja': store1,
                'fornecedor': supplier,
                'data_recebimento': formatted_date,
                'nf': nf,
                'timestamp': formatted_timestamp
            }
            mycolection.insert_one(data_to_insert)
            st.success("Dados enviados com sucesso!")