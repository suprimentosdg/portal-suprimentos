import streamlit as st
import pandas as pd
import os
from io import BytesIO
from xlsxwriter import Workbook

st.set_page_config(page_title="Código dos Produtos")
col1, col2 = st.columns([6, 1])
col1.title("Portal de Suprimentos")
image_path = "logo_globo.png"
image = col2.image(image_path, width=80)
st.subheader("Códigos dos Produtos")
st.write("---")

regions = ["Piauí", "Maranhão", "Rio Grande do Norte", "Bahia", "Pará"]
storesPI = ["15","16","17","18","19","20","21","22","23","24","25","26","29","31","33","36","37","38","39","40","45","66","86","141","144","158","193","200","201","204","205","207","208","209","210","211","215","216","217","219","220","221","223","224","225","226","227","228","229","230","231","232","233","234","235","236","237","238","244","259","260"]
storesMA = ["27","28","30","32","34","35","44","74","76","77","152","239","240","241","242","243","245","246","247","248","249","250","251","252","253","254","255","256","257","258","261","262","263"]
storesRN = ["117","123","302","303","304","305","306","308","309","310","311","314","317","318"," 319","320","321","329","331","334","335","337","338","340"]
storesBA = ["161","162","163","164","165","169","171","176","178","179","181","182","184","186","187","190"]
storesPA = ["80","81","82","83","84","85","87","89","90","91","95","298"]

col1, col2, col3 = st.columns([0.8, 0.6, 1.2])
cod_region = col1.selectbox("Selecione sua Regional:", regions)
with st.container():
    if cod_region == "Piauí":
        cod_store = col2.selectbox("Selecione sua Loja:", storesPI)
        if cod_store == "20" or cod_store == "25" or cod_store == "31" or cod_store == "33" or cod_store == "38" or cod_store == "204" or cod_store == "205" or cod_store == "236":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqPI = "PI_ssoservi_sservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqPI)
            checkPI = pd.read_excel(arqpath)
            st.dataframe(checkPI)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkPI.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "15" or cod_store == "208":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqPI = "PI_ssoservi_sservico_csala.xlsx"
            arqpath = os.path.join("pages", arqPI)
            checkPI = pd.read_excel(arqpath)
            st.dataframe(checkPI)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkPI.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "29" or cod_store == "37" or cod_store == "45" or cod_store == "244" or cod_store == "259"  or cod_store == "260"or cod_store == "16" or cod_store == "17" or cod_store == "18" or cod_store == "19" or cod_store == "21" or cod_store == "22" or cod_store == "23" or cod_store == "26" or cod_store == "36" or cod_store == "39" or cod_store == "40" or cod_store == "66" or cod_store == "86" or cod_store == "141" or cod_store == "144" or cod_store == "158" or cod_store =="200" or cod_store == "209" or cod_store == "210" or cod_store == "211" or cod_store == "215" or cod_store == "216" or cod_store == "217" or cod_store == "219" or cod_store == "220" or cod_store == "221" or cod_store == "223" or cod_store == "224" or cod_store == "225" or cod_store == "226" or cod_store == "227" or cod_store == "228" or cod_store == "229" or cod_store == "230" or cod_store == "231" or cod_store == "232" or cod_store == "233" or cod_store == "234" or cod_store == "235" or cod_store == "237" or cod_store =="238":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqPI = "PI_ssoservi_cservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqPI)
            checkPI = pd.read_excel(arqpath)
            st.dataframe(checkPI)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkPI.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "24" or cod_store == "193" or cod_store == "201" or cod_store == "207":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqPI = "PI_ssoservi_cservico_csala.xlsx"
            arqpath = os.path.join("pages", arqPI)
            checkPI = pd.read_excel(arqpath)
            st.dataframe(checkPI)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkPI.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    elif cod_region == "Maranhão":
        cod_store = col2.selectbox("Selecione sua Loja:", storesMA)
        if cod_store == "28" or cod_store == "44" or cod_store == "257":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqMA = "MA_ssoservi_sservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqMA)
            checkMA = pd.read_excel(arqpath)
            st.dataframe(checkMA)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkMA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "27" or cod_store == "30" or cod_store == "32" or cod_store == "34" or cod_store == "35" or cod_store == "74" or cod_store == "76" or cod_store == "77" or cod_store == "152" or cod_store == "239" or cod_store == "240" or cod_store == "241" or cod_store == "242" or cod_store == "245" or cod_store == "246" or cod_store == "247" or cod_store == "248" or cod_store == "249" or cod_store == "250" or cod_store == "251" or cod_store == "252" or cod_store == "253" or cod_store == "254" or cod_store == "255" or cod_store == "256" or cod_store == "258" or cod_store == "261" or cod_store == "262" or cod_store == "263":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqMA = "MA_ssoservi_cservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqMA)
            checkMA = pd.read_excel(arqpath)
            st.dataframe(checkMA)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkMA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "243":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqMA = "MA_ssoservi_cservico_csala.xlsx"
            arqpath = os.path.join("pages", arqMA)
            checkMA = pd.read_excel(arqpath)
            st.dataframe(checkMA)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkMA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    elif cod_region == "Rio Grande do Norte":
        cod_store = col2.selectbox("Selecione sua Loja:", storesRN)
        if cod_store == "117" or cod_store == "123" or cod_store == "303" or cod_store == "304" or cod_store == "305" or cod_store == "309" or cod_store == "311" or cod_store == "314" or cod_store == "317" or cod_store == "318" or cod_store == "321" or cod_store == "329" or cod_store == "334" or cod_store == "335" or cod_store == "337" or cod_store == "340":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqRN = "RN_csoservi_cservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqRN)
            checkRN = pd.read_excel(arqpath)
            st.dataframe(checkRN)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkRN.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "302" or cod_store == "338":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqRN = "RN_csoservi_cservico_csala.xlsx"
            arqpath = os.path.join("pages", arqRN)
            checkRN = pd.read_excel(arqpath)
            st.dataframe(checkRN)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkRN.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "319":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqRN = "RN_csoservi_sservico_csala.xlsx"
            arqpath = os.path.join("pages", arqRN)
            checkRN = pd.read_excel(arqpath)
            st.dataframe(checkRN)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkRN.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "306" or cod_store == "308" or cod_store == "310" or cod_store == "320" or cod_store == "331":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqRN = "RN_csoservi_sservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqRN)
            checkRN = pd.read_excel(arqpath)
            st.dataframe(checkRN)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkRN.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    elif cod_region == "Bahia":
        cod_store = col2.selectbox("Selecione sua Loja:", storesBA)
        if cod_store == "163" or cod_store == "169" or cod_store == "171" or cod_store == "179" or cod_store == "182":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqBA = "BA_ssoservi_sservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqBA)
            checkBA = pd.read_excel(arqpath)
            st.dataframe(checkBA)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkBA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "161" or cod_store == "162" or cod_store == "171" or cod_store == "176" or cod_store == "186":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqBA = "BA_csoservi_sservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqBA)
            checkBA = pd.read_excel(arqpath)
            st.dataframe(checkBA)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkBA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "165" or cod_store == "178" or cod_store == "190":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqBA = "BA_csoservi_cservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqBA)
            checkBA = pd.read_excel(arqpath)
            st.dataframe(checkBA)     

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkBA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )   
        elif cod_store == "164" or cod_store == "181" or cod_store == "184":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqBA = "BA_ssoservi_cservico_csala.xlsx"
            arqpath = os.path.join("pages", arqBA)
            checkBA = pd.read_excel(arqpath)
            st.dataframe(checkBA)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkBA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "187":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqBA = "BA_csoservi_cservico_csala.xlsx"
            arqpath = os.path.join("pages", arqBA)
            checkBA = pd.read_excel(arqpath)
            st.dataframe(checkBA) 

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkBA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )                  

    elif cod_region == "Pará":
        cod_store = col2.selectbox("Selecione sua Loja:", storesPA)
        if cod_store == "80" or cod_store == "81" or cod_store == "82" or cod_store == "83" or cod_store == "84" or cod_store == "85" or cod_store == "87" or cod_store == "90" or cod_store == "91" or cod_store == "95":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqPA = r"PA_csoservi_cservico_ssala.xlsx"
            arqpath = os.path.join("pages", arqPA)
            checkPA = pd.read_excel(arqpath)
            st.dataframe(checkPA)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkPA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        elif cod_store == "89" or cod_store == "298":
            st.subheader(f"Checklist de Compras da Loja {cod_store}")
            arqPA = r"PA_csoservi_cservico_csala.xlsx"
            arqpath = os.path.join("pages", arqPA)
            checkPA = pd.read_excel(arqpath)
            st.dataframe(checkPA)

            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
                checkPA.to_excel(writer, index=False, header=True)
            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Baixar Checklist",
                data=excel_bytes,
                file_name=f"checklist_loja_{cod_store}.xlsx",
                key="download_button",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )