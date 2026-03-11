import streamlit as st
import pandas as pd
import ollama

# -----------------------------
# Interface
# -----------------------------

st.title("FinAssist 💰")
st.write("Assistente financeiro com IA local (Ollama)")

# salário
salario = st.number_input("Digite seu salário mensal:", min_value=0.0)

st.write("### Registre seus gastos")

# gastos
aluguel = st.number_input("Aluguel", min_value=0.0)
comida = st.number_input("Comida", min_value=0.0)
transporte = st.number_input("Transporte", min_value=0.0)
lazer = st.number_input("Lazer", min_value=0.0)
outros = st.number_input("Outros gastos", min_value=0.0)

# botão
if st.button("Calcular Finanças"):

    total_gastos = aluguel + comida + transporte + lazer + outros
    saldo = salario - total_gastos

    st.write("## Resultado financeiro")

    st.write(f"Total de gastos: R$ {total_gastos}")
    st.write(f"Saldo restante: R$ {saldo}")

    # -----------------------------
    # Criando tabela
    # -----------------------------

    dados = {
        "Categoria": ["Aluguel", "Comida", "Transporte", "Lazer", "Outros"],
        "Valor": [aluguel, comida, transporte, lazer, outros]
    }

    df = pd.DataFrame(dados)

    st.write("### Tabela de gastos")
    st.dataframe(df)

    # gráfico
    st.write("### Gráfico de gastos")
    st.bar_chart(df.set_index("Categoria"))

    # -----------------------------
    # IA analisando as finanças
    # -----------------------------

    prompt = f"""
    Analise as finanças abaixo e dê dicas simples de economia.

    Salário: {salario}
    Total de gastos: {total_gastos}
    Saldo: {saldo}

    Gastos por categoria:
    {df}

    Explique de forma simples onde o usuário pode economizar.
    """

    resposta = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.write("### 🤖 Análise da IA")
    st.write(resposta["message"]["content"])