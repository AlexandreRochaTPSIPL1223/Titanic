import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import sqlite3

#3.1 Leitura e exploração dos dados

file_path = ('titanic (1).csv') #Caminho do .csv
df = pd.read_csv(file_path) #Ler o .csv

print(f"\nPrimeiros Registos:\n {df.head()}") #Escrever o primeiros registo no .csv
print(f"\nUltimos Registos:\n {df.tail()}") #Escrever o últimos registo no .csv

print(f"\nInformações do DataFrame:\n {df.info()}")
print(f"\nEstatísticas descritivas do DataFrame:\n {df.describe()}")


print("\n##################################################################################################################################")
#3.2 Limpeza e pré-processamento de dados

print(f"\nValores nulos por coluna:\n{df.isnull().sum()}")

df['Age'].fillna(df['Age'].mean(), inplace=True) #Preencher valores nulos com a média das idades para não afetar a média geral das idades
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True) #Substituir valores nulos pelo valor mais frequente
df.drop(columns=['Cabin'], inplace=True) # Remoção da coluna "Cabin" devido a uma grande quantidade de valores nulos

df['Age'] = df['Age'].astype(float) #Ages são float

epoch = datetime(1970, 1, 1)
df['Idade_Milissegundos'] = df['Age'].apply(lambda x: int((epoch + pd.Timedelta(days=x*365)).timestamp() * 1000)) #Converte a idade para milissegundos desdo "epoch"

print(f"\nDataFrame após limpeza e pré-processamento de dados:\n {df.head()}")

print("\n##################################################################################################################################")
#3.3 Análise e manipulação de dados

taxa_sobrevivencia = df.groupby(['Pclass', 'Sex'])['Survived'].mean().reset_index() #Relação entre sobrevivência e classe/sexo
print(f"\nTaxa de sobrevivência (por classe e sexo):\n {taxa_sobrevivencia}")

idade_sobrevivencia = df.groupby(['Survived'])['Age'].mean().reset_index() #Relação entre idade e sobrevivência
print(f"\nIdade média por status de sobrevivência:\n {idade_sobrevivencia}")

tarifa_classe_sexo = df.groupby(['Pclass', 'Sex'])['Fare'].mean().reset_index() #Relação entre tarifa e classe/sexo
print(f"\nTarifa média por classe e sexo:\n {tarifa_classe_sexo}")

correlacao_tarifa_sobrevivencia = df[['Fare', 'Survived']].corr().iloc[0, 1]
print("\nPositivo (>0) -> Tarifas mais altas = Maior Probabilidade de sobrevivência\n")
print("Negativo (<0) -> Tarifas mais altas = Menor Probabilidade de Sobrevivência\n")
print("Próximo de 0 -> Relação entre a tarifa e sobrevivencia é inconsequente\n")
print(f"Correlação entre Tarifa e Sobrevivência:\n {correlacao_tarifa_sobrevivencia:.2f}")

print("\n##################################################################################################################################")
#3.4 Visualização de dados

#Distribuição de sobreviventes por classe e sexo (Gráfico de barras)
plt.figure(figsize = (8,6))
grafico1 = sns.countplot(data=df, x='Pclass', hue='Sex', palette='rocket')
plt.title("Distribuição de Sobreviventes por Classe e Sexo")
plt.xlabel("Classe")
plt.ylabel("Número de Passageiros")
plt.legend(title='Sexo')
plt.tight_layout()
plt.show()

#Correlação entre Age, Fare e Survived(Gráfico de dispersão (scatter plots))
plt.figure(figsize = (8,6))
grafico2 = sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', palette='coolwarm')
plt.title("Correlação entre Idade, Tarifa e Sobrevivência")
plt.xlabel("Idade")
plt.ylabel("Tarifa")
plt.legend(title="Sobreviveu")
plt.tight_layout()
plt.show()

#Histogramas para visualisar a distribuição de Age, Fare, e Survived
grafico3 = df[['Age', 'Fare', 'Survived']].hist(figsize=(10, 8), bins=20)
plt.tight_layout()
plt.show()

print("\nVisualização dos gráficos")
print("\n##################################################################################################################################")
# 3.5 Exportação dos Resultados

# Exporta o DataFrame atualizado para Excel
output_excel = "titanic_resultados.xlsx"
df.to_excel(output_excel, index=False)
print(f"\nDataFrame exportado para '{output_excel}'.")

# Guardar os gráficos
plt.figure(figsize=(8, 6))
grafico1.figure.savefig("grafico_sobrevivencia_classe_sexo.png")
plt.close()

plt.figure(figsize=(8, 6))
grafico2.figure.savefig("grafico_correlacao_age_fare.png")
plt.close()

plt.figure(figsize=(10, 8))
fig3 = plt.figure()
df[['Age', 'Fare', 'Survived']].hist(figsize=(10, 8), bins=20)
plt.tight_layout()
fig3.savefig("grafico_histogramas_age_fare_survived.png")
plt.close()

# 3.6 Armazenamento numa Base de Dados

# Conectar a um banco SQLite
conn = sqlite3.connect("titanic_data.db")
cursor = conn.cursor()

# Criar tabela no SQLite
cursor.execute("""
CREATE TABLE IF NOT EXISTS Titanic (
    PassengerId INTEGER PRIMARY KEY,
    Pclass INTEGER,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    SibSp INTEGER,
    Parch INTEGER,
    Ticket TEXT,
    Fare REAL,
    Embarked TEXT,
    Survived INTEGER,
    Idade_Milissegundos INTEGER
)
""")

# Inserir os dados na DB
df.to_sql("Titanic", conn, if_exists="replace", index=False)
print("\nDados armazenados na base de dados 'titanic_data.db'")

# Fechar conexão
conn.close()

