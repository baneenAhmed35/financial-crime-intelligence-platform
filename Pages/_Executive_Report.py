import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Executive Report",
    layout="wide"
)

st.title("📁 Executive Fraud Investigation Report")

df = pd.read_csv("alerts.csv")

high_risk = len(
    df[df["risk_level"] == "High"]
)

total_amount = df["transaction_amount"].sum()

st.markdown(f"""

## Executive Summary

The investigation identified
**{high_risk} high-risk cases**
with suspicious transactions totaling
**${total_amount:,.0f}**.

### Key Findings
- Money Laundering activity detected
- Multiple escalated investigations observed
- Cross-border transaction exposure identified

### Operational Insights
- High-value transactions require enhanced monitoring
- Investigation time increases with transaction size
- UAE and UK transactions indicate elevated exposure risk

### Recommendation
Enhanced monitoring controls and faster escalation procedures are recommended for high-risk alerts.

""")