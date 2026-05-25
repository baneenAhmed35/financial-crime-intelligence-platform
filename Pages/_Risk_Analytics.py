import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Risk Analytics",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("alerts.csv")
# =========================
# AI RISK SCORING
# =========================

df["ai_risk_score"] = (
    df["transaction_amount"] / 300
    + df["investigation_hours"] * 4
)

df["ai_risk_score"] = (
    df["ai_risk_score"]
    .clip(0, 100)
    .round(0)
)

# =========================
# TITLE
# =========================

st.title("📊 Risk Analytics Center")

st.markdown("""
### Enterprise Risk Monitoring & Financial Crime Exposure Analysis
""")

st.caption(
    "Advanced analysis of operational risk levels, investigation severity, and AI-driven fraud exposure scoring"
)

# =========================
# KPI SECTION
# =========================

high_risk = len(df[df["risk_level"] == "High"])

avg_score = round(
    df["ai_risk_score"].mean(),
    1
)

max_score = int(
    df["ai_risk_score"].max()
)

total_amount = df["transaction_amount"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "High Risk Cases",
    high_risk
)

col2.metric(
    "Average AI Risk Score",
    avg_score
)

col3.metric(
    "Maximum Risk Score",
    max_score
)

col4.metric(
    "Suspicious Exposure",
    f"${total_amount:,.0f}"
)

st.divider()

# =========================
# EXECUTIVE INSIGHT
# =========================

st.warning(f"""
AI monitoring identified elevated financial crime exposure
associated with high-value cross-border transactions.

Current average AI risk score is {avg_score},
with maximum exposure reaching {max_score}/100.

Enhanced monitoring is recommended for escalated investigations
related to money laundering and wire fraud patterns.
""")

# =========================
# RISK DISTRIBUTION
# =========================

fig_pie = px.pie(
    df,
    names="risk_level",
    title="Risk Distribution",
    color="risk_level",
    color_discrete_map={
        "High": "#FF4B4B",
        "Medium": "#FFA500",
        "Low": "#00C853"
    }
)

fig_pie.update_layout(
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white",
    height=500
)

# =========================
# AI SCORE ANALYSIS
# =========================

fig_score = px.scatter(
    df,
    x="transaction_amount",
    y="ai_risk_score",
    color="risk_level",
    size="ai_risk_score",
    hover_data=["fraud_type", "country"],
    title="AI Risk Score Analysis",
    color_discrete_map={
        "High": "#FF4B4B",
        "Medium": "#FFA500",
        "Low": "#00C853"
    }
)

fig_score.update_layout(
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white",
    height=500
)

# =========================
# LAYOUT
# =========================

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

with col6:
    st.plotly_chart(
        fig_score,
        use_container_width=True
    )

# =========================
# INVESTIGATION TIME
# =========================

fig_time = px.bar(
    df,
    x="fraud_type",
    y="investigation_hours",
    color="risk_level",
    title="Investigation Time by Fraud Type",
    color_discrete_map={
        "High": "#FF4B4B",
        "Medium": "#FFA500",
        "Low": "#00C853"
    }
)

fig_time.update_layout(
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white",
    height=500
)

st.plotly_chart(
    fig_time,
    use_container_width=True
)

# =========================
# RISK TABLE
# =========================

st.subheader("📌 AI Risk Classification Table")

display_df = df[
    [
        "alert_id",
        "risk_level",
        "ai_risk_score",
        "transaction_amount",
        "country",
        "fraud_type"
    ]
]

styled_df = display_df.style.background_gradient(
    subset=["ai_risk_score"],
    cmap="Reds"
)

st.dataframe(
    styled_df,
    use_container_width=True
)