import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

# Configurações da página
st.set_page_config(
    page_title="Análise Titanic 🚢",
    page_icon="🚢",
    layout="wide"
)


# Função para carregar e processar os dados
@st.cache_data
def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df.drop(columns=['Cabin'], inplace=True)
    df['Idade_Milissegundos'] = df['Age'].apply(lambda x: int(x * 365 * 24 * 60 * 60 * 1000))
    return df


# Função para armazenar no SQLite
def armazenar_dados(df):
    conn = sqlite3.connect("titanic_data.db")
    df.to_sql("Titanic", conn, if_exists="replace", index=False)
    conn.close()


# Carregar os dados
caminho = 'titanic (1).csv'
df = carregar_dados(caminho)

# Menu principal
menu = st.sidebar.selectbox("Navegação", ["Página Inicial", "Análise de Dados", "Visualização", "Exportação"])

# Página inicial
if menu == "Página Inicial":
    st.image("RMS_Titanic_3.jpg", width=700)
    st.title("Análise de Dados do Titanic 🚢")
    st.write(
        """
        Página web criada no ambito da UFCD 5417, com o objetivo de demonstrar os scripts do Projeto1 a correr numa página web
        """
    )

# Análise de Dados
elif menu == "Análise de Dados":
    st.title("Análise de Dados 📊")

    # Taxa de sobrevivência por classe e sexo
    st.subheader("Taxa de Sobrevivência (por Classe e Sexo)")
    taxa_sobrevivencia = df.groupby(['Pclass', 'Sex'])['Survived'].mean().reset_index()
    st.write(taxa_sobrevivencia)

    # Idade média por status de sobrevivência
    st.subheader("Idade Média por Status de Sobrevivência")
    idade_sobrevivencia = df.groupby(['Survived'])['Age'].mean().reset_index()
    st.write(idade_sobrevivencia)

    # Tarifa média por classe e sexo
    st.subheader("Tarifa Média por Classe e Sexo")
    tarifa_classe_sexo = df.groupby(['Pclass', 'Sex'])['Fare'].mean().reset_index()
    st.write(tarifa_classe_sexo)

    # Correlação entre Tarifa e Sobrevivência
    correlacao_tarifa_sobrevivencia = df[['Fare', 'Survived']].corr().iloc[0, 1]
    st.subheader("Correlação entre Tarifa e Sobrevivência")
    st.write(f"A correlação é de {correlacao_tarifa_sobrevivencia:.2f}.")

# Visualização de Gráficos
elif menu == "Visualização":
    st.title("Visualização de Gráficos")

    # Gráfico 1: Distribuição por Classe e Sexo
    st.subheader("Distribuição por Classe e Sexo")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='Pclass', hue='Sex', palette='rocket', ax=ax1)
    st.pyplot(fig1)

    # Gráfico 2: Correlação entre Idade e Tarifa
    st.subheader("Correlação entre Idade e Tarifa")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', palette='coolwarm', ax=ax2)
    st.pyplot(fig2)

    # Gráfico 3: Histogramas
    st.subheader("Histogramas de Age, Fare e Survived")
    fig3, ax3 = plt.subplots(figsize=(10, 8))
    df[['Age', 'Fare', 'Survived']].hist(bins=20, ax=ax3)
    st.pyplot(fig3)
# Exportação
elif menu == "Exportação":
    st.title("Exportação de Resultados 💾")

    # Botão para exportar DataFrame
    if st.button("Exportar para Excel"):
        df.to_excel("titanic_resultados.xlsx", index=False)
        st.success("Arquivo Excel exportado como 'titanic_resultados.xlsx'")

    # Botão para armazenar no SQLite
    if st.button("Armazenar no Banco de Dados"):
        armazenar_dados(df)
        st.success("Dados armazenados no banco de dados SQLite 'titanic_db.db'")
