import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Live Alerts",
    layout="wide"
)

st.title("🚨 Live Fraud Alerts Monitor")

df = pd.read_csv("../alerts.csv")

critical_alerts = df[
    df["risk_level"] == "High"
]

st.error(
    f"{len(critical_alerts)} Critical Alerts Require Immediate Attention"
)

for _, row in critical_alerts.iterrows():

    risk_score = random.randint(85, 99)

    st.warning(f"""
    ALERT ID: {row['alert_id']}

    Fraud Type: {row['fraud_type']}

    Country: {row['country']}

    Suspicious Amount: ${row['transaction_amount']:,.0f}

    AI Risk Score: {risk_score}/100
    """)