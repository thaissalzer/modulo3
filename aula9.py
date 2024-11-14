import streamlit as st
import pandas as pd

st.title('Aplicação de filtragem de dataframes')

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})

st.write("Criando uma tabela!")
st.write(df)

opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])
