import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import random
from src.app.schemas import (
    JobEnum, MaritalEnum, EducationEnum, ContactEnum, 
    YesNoEnum, MonthEnum, PoutcomeEnum, MarketingLead
)

## Para rodar -> streamlit run streamlit/streamlit_app.py

load_dotenv()

# Defining options:
job_options = [job.value for job in JobEnum]
marital_options = [marital.value for marital in MaritalEnum]
education_options = [education.value for education in EducationEnum]
yes_no_options = [yes_no.value for yes_no in YesNoEnum]
contact_options = [contact.value for contact in ContactEnum]
month_options = [month.value for month in MonthEnum]
poutcome_options = [poutcome.value for poutcome in PoutcomeEnum]

# Streamlit start
st.title("📊 Previsão de Lead - Best Sale")

st.write("Preencha as informações do cliente para prever se ele fechará o depósito a prazo.")

age = st.number_input("Idade", min_value=18, max_value=100)
job = st.selectbox("Profissão", job_options)
marital = st.selectbox("Estado civil", marital_options)
education = st.selectbox("Educação", education_options)
default = st.selectbox("Possui crédito em default?", yes_no_options)
balance = st.number_input("Saldo médio anual", min_value=0)
housing = st.selectbox("Possui financiamento habitacional?", yes_no_options)
loan = st.selectbox("Possui empréstimo pessoal?", yes_no_options)
contact = st.selectbox("Tipo de contato", contact_options)
month = st.selectbox("Mês da última ligação", month_options)
day_of_month = st.slider("Dia da última ligação (1-31)", 1, 31)
campaign = st.number_input("Nº de contatos nesta campanha", min_value=1, max_value=50)
pdays = st.number_input("Dias desde último contato (-1 = nunca)", min_value=-1, max_value=999, value=-1)
previous = st.number_input("Nº de contatos anteriores", min_value=0, max_value=50)
poutcome = st.selectbox("Resultado da campanha anterior", poutcome_options)

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

# Button to Send Data and Make Prediction
if st.button("Make Prediction"):
    # Create a MarketingLead instance with the form data
    try:
        lead_data = MarketingLead(
            age=age,
            job=job,
            marital=marital,
            education=education,
            default=default,
            balance=balance,
            housing=housing,
            loan=loan,
            contact=contact,
            day_of_month=day_of_month,
            month=month,
            campaign=campaign,
            pdays=pdays,
            previous=previous,
            poutcome=poutcome,
        )

        # Convert the Pydantic object to a dictionary
        lead_dict = lead_data.model_dump()

        api_url = os.getenv('FASTAPI_URL')
        if not api_url:
            st.error("FASTAPI_URL not found. Please set it in your .env file.")
        else:
            st.write("Sending the following data to the API:", lead_dict)

            response = requests.post(f"{api_url}/predict", json=lead_dict)
            response.raise_for_status()  # This will raise an error if the response is not 200 OK
            prediction = response.json()
            st.success(f"Prediction Result: {prediction}")

    except Exception as e:
        st.error(f"An error occurred while making the prediction: {e}")