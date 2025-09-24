import streamlit as st
import pandas as pd
import random

## Para rodar -> streamlit run streamlit/streamlit_app.py

st.title("📊 Previsão de Lead - Best Sale")

st.write("Preencha as informações do cliente para prever se ele fechará o depósito a prazo.")

age = st.number_input("Idade", min_value=18, max_value=100)
job = st.selectbox("Profissão", ["admin", "blue-collar", "entrepreneur", "housemaid",
                                  "management", "retired", "self-employed", "services",
                                  "student", "technician", "unemployed"])
marital = st.selectbox("Estado civil", ["single", "married", "divorced"])
education = st.selectbox("Educação", ["primary", "secondary", "tertiary", "unknown"])
default = st.selectbox("Possui crédito em default?", ["no", "yes"])
balance = st.number_input("Saldo médio anual", min_value=0)
housing = st.selectbox("Possui financiamento habitacional?", ["no", "yes"])
loan = st.selectbox("Possui empréstimo pessoal?", ["no", "yes"])
contact = st.selectbox("Tipo de contato", ["cellular", "telephone"])
month = st.selectbox("Mês da última ligação", 
                     ["jan", "feb", "mar", "apr", "may", "jun", 
                      "jul", "aug", "sep", "oct", "nov", "dec"])
day_of_week = st.slider("Dia da última ligação (1-31)", 1, 31)
duration = st.number_input("Duração da ligação (segundos)", min_value=0, max_value=5000)
campaign = st.number_input("Nº de contatos nesta campanha", min_value=1, max_value=50)
pdays = st.number_input("Dias desde último contato (-1 = nunca)", min_value=-1, max_value=999, value=-1)
previous = st.number_input("Nº de contatos anteriores", min_value=0, max_value=50)
poutcome = st.selectbox("Resultado da campanha anterior", ["success", "failure", "other", "unknown"])

# BOTAO MOCK
if st.button("🔍 Simular fechamento do lead"):
    # PROB: 0 - 1
    prob = random.random()
    prediction = "yes" if prob > 0.5 else "no"

    if prediction == "yes":
        st.success(f"✅ O lead TEM ALTA chance de fechar! (Probabilidade simulada: {prob:.2%})")
    else:
        st.error(f"❌ O lead provavelmente NÃO fechará. (Probabilidade simulada: {prob:.2%})")

    st.subheader("📋 Resumo dos inputs preenchidos")
    input_data = pd.DataFrame([{
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "balance": balance,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "month": month,
        "day_of_week": day_of_week,
        "duration": duration,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous,
        "poutcome": poutcome
    }])
    st.dataframe(input_data)