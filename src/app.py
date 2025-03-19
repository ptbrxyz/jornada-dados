import pandas as pd
import streamlit as st
from pydantic import BaseModel, Field, condecimal, conint, ValidationError
from datetime import date
from validador import Validador


# Função para validar cada linha do CSV usando o modelo Validador
def validar_linhas_csv(dados_csv):
    validacoes = []
    for index, row in dados_csv.iterrows():
        try:
            # Tenta validar a linha utilizando o modelo Pydantic
            validador = Validador(**row.to_dict())
            validacoes.append((index, "Válido"))
        except ValidationError as e:
            # Caso haja erro de validação, adiciona a mensagem de erro
            validacoes.append((index, f"Inválido: {e}"))
    return validacoes

# Função principal para criar a interface de upload e exibir os resultados
def main():
    # Título da aplicação
    st.title("Validador de Planilhas CSV")

    # Upload de arquivo CSV
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        # Lê o arquivo CSV usando pandas
        dados_csv = pd.read_csv(uploaded_file)

        # Exibe as primeiras linhas do CSV
        st.write("Primeiras linhas do CSV:")
        st.write(dados_csv.head())

        # Valida as linhas do CSV
        validacoes = validar_linhas_csv(dados_csv)

        # Exibe os resultados de validação
        st.write("Resultado da Validação das Linhas:")
        for idx, resultado in validacoes:
            if "Inválido" in resultado:
                st.error(f"Linha {idx + 1}: {resultado}")
            else:
                st.success(f"Linha {idx + 1}: {resultado}")

# Executa a aplicação Streamlit
if __name__ == "__main__":
    main()
