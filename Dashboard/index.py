import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def main():
    st.title("Titulo ENEMInsights")
    st.write("ENEMInsights é uma ferramenta desenvolvida para traçar o perfil dos participantes do ENEM, utilizando dados disponibilizados pelo governo no site gov.br. A partir desses dados, o ENEMInsights estabelece uma relação entre a realidade socioeconômica e o desempenho dos participantes na prova. Este projeto foi criado como parte do trabalho final da disciplina de Probabilidade e Estatística do curso de Tecnologia em Redes de Computadores do IFRN (Instituto Federal do Rio Grande do Norte).")
    #Uploaded dos dados
    st.header("Uploaded dos dados")
    uploaded_file = st.file_uploader("Escolher um arquivo", type=["txt", "csv", "pdf"])
    if uploaded_file:
        st.write("Nome do arquivo: ", uploaded_file.name)

    st.title("Filtro")
    #Seleção de ano
    st.header("Seleção")
    selected_option = st.selectbox("Selecione uma opção", ["2023", "2022", "2021"])
    if selected_option:
        st.write("Ano: ", selected_option)

    #Seleção de dados socioeconômico
    st.header("Dados: ")
    checkbox_state_cel = st.checkbox("Aparelho celular", "Internet", "Computador")
    checkbox_state_int = st.checkbox("Internet")
    checkbox_state_comput = st.checkbox("Computador")
    st.write("Celular", checkbox_state_cel, "Internet", checkbox_state_int, "Computador", checkbox_state_comput)

    #Seleção de renda
    st.header("Renda familia")
    slider_value = st.slider("Escolha um valor", 0, 1908000)
    st.write("Valor: ", slider_value)
    #Gráfico
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)

    #Dados de exemplo
    data = {
        'Categoria': ['A', 'B', 'C', 'D'],
        'Valores': [10, 20, 30, 40]
    }

    #Criando um DataFrame
    df = pd.DataFrame(data)

    #Título do aplicativo
    st.title('Gráfico de Colunas com Streamlit')

    #Exibindo o gráfico de colunas
    st.bar_chart(df.set_index('Categoria'))

    #Gráfico 02
    #Dados de exemplo
    data = {
        'Categoria': ['A', 'B', 'C', 'D'],
        'Valores': [10, 20, 30, 40]
    }

    #Criando um DataFrame
    df = pd.DataFrame(data)

    #Título do aplicativo
    st.title('Gráfico de Colunas com Matplotlib')

    #Criando o gráfico com Matplotlib
    fig, ax = plt.subplots()
    ax.bar(df['Categoria'], df['Valores'])
    ax.set_xlabel('Categoria')
    ax.set_ylabel('Valores')
    ax.set_title('Gráfico de Colunas')

    #Exibindo o gráfico no Streamlit
    st.pyplot(fig)


main()
