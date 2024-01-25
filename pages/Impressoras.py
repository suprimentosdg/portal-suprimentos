import streamlit as st
from datetime import datetime
from pymongo import MongoClient

regions = ["Piauí", "Maranhão", "Rio Grande do Norte", "Bahia", "Pará"]

connectString = "mongodb+srv://suprimentosdglobo:suprimentosdg2023@cluster0.dx7yrgp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connectString)
db = client["confirmations"]
mycolection = db.Cl02

st.set_page_config(page_title="Impressoras")
st.title("Portal de Suprimentos")
st.subheader("Abertura de chamado para Impressora")

with st.form(key="include_called"):
    name2 = st.text_input("Digite seu nome:")
    region2 = st.selectbox("Selecione sua regional:", regions)
    store2 = st.number_input("Digite sua loja:", min_value=0, max_value=999)
    printerTypes = st.selectbox("Selecione seu modelo de impressora:", ["BROTHER DCP 8157","BROTHER DCP 1602","BROTHER DCP 1617","BROTHER DCP 1617","BROTHER DCP 7065","BROTHER DCP 7460","BROTHER DCP 7860","BROTHER DCP 8112","BROTHER DCP 8152","BROTHER DCP 8912","CANON G2110","CANON G3111","HP LASER JET M428","HP LASER JET M 1132","HP LASER JET M 1536","HP LASER JET M127","HP LASER JET M1536","HP LASER JET M225","HP LASER JET M426","HP LASER JETM125","HP LASERJE TM125","HP LASERJET M1132","HP LASERJET M1212","HP LASERJET M127"])
    options = st.selectbox("Escolha uma opção:", ["Solicitação de toner", "Assistência técnica"])
    obs = st.text_area("Obs.:", placeholder="Em caso de chamado para assistência técnica, informe o motivo da solicitação.")
    send2 = st.form_submit_button("Enviar")
    if send2:
        current_timestamp = datetime.now().timestamp()
        formatted_timestamp = datetime.fromtimestamp(current_timestamp).strftime("%d/%m/%Y %H:%M:%S")

        if not name2 or not region2 or not store2 or not printerTypes or not options:
            st.warning("Por favor, preencha todos os campos.")
        elif options == "Assistência técnica" and not obs:
            st.warning("Por favor, preencha o motivo da abertura do chamado.")

        else:
            data_to_insert = {
                'nome': name2,
                'regional': region2,
                'loja': store2,
                'impressora': printerTypes,
                'opcao': options,
                'observacao': obs,
                'timestamp': formatted_timestamp
            }
            mycolection.insert_one(data_to_insert)
            st.success("Solicitação enviada com sucesso!")