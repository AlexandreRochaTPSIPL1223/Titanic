# Projeto Titanic - UFCD 5417

## Introdução

Este projeto tem como objetivo explorar e analisar o conjunto de dados do *Titanic*, que contém informações detalhadas sobre os passageiros e os sobreviventes do famoso desastre marítimo de 1912. A análise será realizada com **Python 3**, utilizando as bibliotecas **Pandas** para manipulação de dados e **Matplotlib/Seaborn** para visualização. O projeto inclui atividades de leitura, limpeza, análise, visualização e exportação dos dados, com possibilidade de armazenamento numa base de dados.

---

## Preparar o Ambiente Virtual

Para configurar o ambiente virtual necessário, siga os seguintes passos:

### Pré-requisitos:
- Python 3.x instalado
- Git instalado
- Biblioteca **Streamlit** para criar a interface

### Passos para Preparar o Ambiente:

1. **Clonar o repositório do GitHub**:
   ```bash
   git clone https://github.com/AlexandreRochaTPSIPL1223/Titanic.git
   cd Titanic
   ```

2. **Criar e ativar um ambiente virtual**:
   ```bash
   python -m venv venv
   ```

   ```bash
   .\venv\Scripts\activate
   ```


3. **Instalar as dependências necessárias**:
   ```bash
   pip install -r requirements_pg.txt
   ```
    **Instalar as dependências necessárias para a página web**:
   ```bash
   pip install -r requirements_pg.txt
   ```

---

## Perguntas Realizadas no Projeto

1. Carregar e explorar os dados (primeiros registros, valores nulos, etc.).
2. Criar a coluna `Idade_Milissegundos` convertendo as idades.
3. Analisar taxas de sobrevivência por classe e sexo.
4. Calcular a tarifa média por classe e correlações entre variáveis.
5. Criar gráficos para representar tendências, correlações e distribuições.
6. Exportar os dados e gráficos.
7. Armazenar os dados numa base de dados SQL.

---

## Executar o Script e Streamlit

### Comandos para Executar o Script:

1. **Executar o script principal da análise**:
   ```bash
   python main.py
   ```

2. **Iniciar o Streamlit** (caso haja uma interface interativa desenvolvida):
   ```bash
   streamlit run app.py
   ```

**Nota**: Certifique-se de que o ambiente virtual esteja ativo antes de executar os comandos.

---