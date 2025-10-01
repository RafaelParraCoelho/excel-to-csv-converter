import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Conversor de Excel para CSV")

# Upload do arquivo
uploaded_file = st.file_uploader("Escolha um arquivo Excel (.xlsx)", type="xlsx")

if uploaded_file:
    # Lê todas as abas
    xls = pd.ExcelFile(uploaded_file)
    dfs = []

    for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet)
        df["Origem_Aba"] = sheet  # opcional: saber de qual aba veio
        dfs.append(df)

    # Junta tudo em um único CSV
    final_df = pd.concat(dfs, ignore_index=True)

    # Converte para CSV em memória
    csv_buffer = BytesIO()
    final_df.to_csv(csv_buffer, sep=",", index=False, encoding="utf-8")
    csv_buffer.seek(0)

    # Botão para download
    st.download_button(
        label="Baixar CSV",
        data=csv_buffer,
        file_name="Planilha_Convertida.csv",
        mime="text/csv"
    )
