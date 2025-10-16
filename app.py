# import streamlit as st
# import pandas as pd
# from io import BytesIO

# st.title("Conversor de Excel para CSV")

# # Upload do arquivo
# uploaded_file = st.file_uploader("Escolha um arquivo Excel (.xlsx)", type="xlsx")

# if uploaded_file:
#     # Lê todas as abas
#     xls = pd.ExcelFile(uploaded_file)
#     dfs = []
    
#     for sheet in xls.sheet_names:
#         df = pd.read_excel(xls, sheet_name=sheet)
#         df["Origem_Aba"] = sheet  # opcional: saber de qual aba veio
#         dfs.append(df)

#     # Junta tudo em um único CSV
#     final_df = pd.concat(dfs, ignore_index=True)

#     # Converte para CSV em memória
#     csv_buffer = BytesIO()
#     final_df.to_csv(csv_buffer, sep=",", index=False, encoding="utf-8")
#     csv_buffer.seek(0)

#     # Botão para download
#     st.download_button(
#         label="Baixar CSV",
#         data=csv_buffer,
#         file_name="Planilha_Convertida.csv",
#         mime="text/csv"
#     )

import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Conversor de Excel para CSV)")

uploaded_file = st.file_uploader("Escolha um arquivo Excel (.xlsx)", type="xlsx")

if uploaded_file:
    incluir_origem = st.checkbox("Incluir coluna de origem da aba", value=False)

    xls = pd.ExcelFile(uploaded_file)
    dfs = []
    
    for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet)

        # Remove colunas "Unnamed"
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

        # Remove quebras de linha internas nas células
        df = df.applymap(lambda x: str(x).replace("\n", "").replace("\r", "") if pd.notnull(x) else "")

        if incluir_origem:
            df["Origem_Aba"] = sheet
        
        dfs.append(df)
        
    final_df = pd.concat(dfs, ignore_index=True)

    # Se houver apenas uma coluna, formata como "valor,\n"
    if final_df.shape[1] == 1:
        col = final_df.columns[0]
        valores = final_df[col].astype(str).dropna().tolist()
        csv_str = ",\n".join([v.strip() for v in valores if v.strip() != ""])  # vírgula antes da quebra
        if not csv_str.endswith(","):
            csv_str += ","
    else:
        csv_str = final_df.to_csv(index=False, sep=",", encoding="utf-8")

    # Converte para bytes para download
    csv_buffer = BytesIO(csv_str.encode("utf-8"))

    st.download_button(
        label="Baixar CSV",
        data=csv_buffer,
        file_name="Planilha_Convertida.csv",
        mime="text/csv"
    )
