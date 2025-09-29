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

## Run -> uv run -m streamlit run frontend/streamlit_app.py

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
st.title("📊 Lead Conversion Prediction")
st.write("Welcome to the Lead Conversion Prediction app!")
st.write("This app predicts whether a customer will subscribe to a term deposit based on their information.")
st.write("Fill in the customer information in the sidebar and click the button to get a prediction.")

st.sidebar.header("Customer Information")
age = st.sidebar.number_input("Age", min_value=18, max_value=100)
job = st.sidebar.selectbox("Job", job_options)
marital = st.sidebar.selectbox("Marital Status", marital_options)
education = st.sidebar.selectbox("Education", education_options)
default = st.sidebar.selectbox("Has Credit Default?", yes_no_options)
balance = st.sidebar.number_input("Average Annual Balance", min_value=0)
housing = st.sidebar.selectbox("Has Housing Loan?", yes_no_options)
loan = st.sidebar.selectbox("Has Personal Loan?", yes_no_options)
contact = st.sidebar.selectbox("Contact Type", contact_options)
day_of_month = st.sidebar.slider("Day of Last Contact (1-31)", 1, 31)
month = st.sidebar.selectbox("Month of Last Contact", month_options)
campaign = st.sidebar.number_input("Number of Contacts in Campaign", min_value=1, max_value=50)
pdays = st.sidebar.number_input("Days Since Last Contact (-1 = never)", min_value=-1, max_value=999, value=-1)
previous = st.sidebar.number_input("Number of Previous Contacts Before this Campaign", min_value=0, max_value=50)
poutcome = st.sidebar.selectbox("Previous Campaign Outcome", poutcome_options)

# BOTAO MOCK
#if st.button("🔍 Simular fechamento do lead"):
#   # PROB: 0 - 1
#    prob = random.random()
#    prediction = "yes" if prob > 0.5 else "no"

#    if prediction == "yes":
#        st.success(f"✅ O lead TEM ALTA chance de fechar! (Probabilidade simulada: {prob:.2%})")
#    else:
#       st.error(f"❌ O lead provavelmente NÃO fechará. (Probabilidade simulada: {prob:.2%})")

#    st.subheader("📋 Resumo dos inputs preenchidos")

# Button to Send Data and Make Prediction
if st.sidebar.button("Predict Lead Outcome"):
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
            with st.spinner("Working on it..."):
                response = requests.post(f"{api_url}/predict", json=lead_dict)
                response.raise_for_status()  # This will raise an error if the response is not 200 OK

                result = response.json()
                prediction = result.get("prediction")
                probability = result.get("probability_yes")

                st.header("Result")

                if prediction == 1:
                    st.success(f"✅ The lead is LIKELY to subscribe! (Probability: {probability:.2%})")
                else:
                    st.error(f"❌ The lead is UNLIKELY to subscribe. (Probability: {probability:.2%})")

                with st.expander("📋 Input Summary"):
                    st.json(lead_dict)

    except Exception as e:
        st.error(f"An error occurred while making the prediction: {e}")
