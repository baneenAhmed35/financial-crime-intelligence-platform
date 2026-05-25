import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Geographic Analysis",
    layout="wide"
)

st.title("🌍 Geographic Fraud Analysis")

df = pd.read_csv("alerts.csv")

country_amount = df.groupby(
    "country"
)["transaction_amount"].sum().reset_index()

fig = px.bar(
    country_amount,
    x="country",
    y="transaction_amount",
    color="transaction_amount",
    title="Suspicious Amount by Country"
)

fig.update_layout(
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Country Risk Summary")

st.dataframe(
    country_amount,
    use_container_width=True
)