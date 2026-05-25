# =========================
# IMPORT LIBRARIES
# =========================

import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Financial Crime Intelligence Center",
    page_icon="🚨",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    background: linear-gradient(
        135deg,
        #0B0F19,
        #111827
    );
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3, h4 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.title("🚨 Financial Crime Intelligence Center")

st.markdown("""
### Real-Time Financial Crime Intelligence, Fraud Detection, and AML Investigation Platform
""")

st.caption(
    "Real-time monitoring of suspicious transactions, fraud alerts, and investigation performance"
)

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    r"C:\Users\Banee\OneDrive\سطح المكتب\Alert -Analyzer\alerts.csv"
)

# =========================
# SIDEBAR
# =========================

st.sidebar.success("Financial Crime Navigation")

st.sidebar.markdown("""
---
### Active Monitoring System
- AML Investigation
- Fraud Detection
- AI Risk Scoring
- Transaction Intelligence
---
""")

st.sidebar.header("🔎 Investigation Filters")

selected_risk = st.sidebar.multiselect(
    "Risk Level",
    options=df["risk_level"].unique(),
    default=df["risk_level"].unique()
)

selected_country = st.sidebar.multiselect(
    "Country",
    options=df["country"].unique(),
    default=df["country"].unique()
)

selected_work_country = st.sidebar.selectbox(
    "🌍 Investigation Region",
    [
        "Saudi Arabia",
        "UAE",
        "UK",
        "USA",
        "Bahrain",
        "Kuwait"
    ]
)

st.sidebar.info(
    f"Active Intelligence Region: {selected_work_country}"
)

# =========================
# FILTER DATA
# =========================

filtered_df = df[
    (df["risk_level"].isin(selected_risk)) &
    (df["country"].isin(selected_country))
]

# =========================
# AI RISK SCORING
# =========================

filtered_df = filtered_df.copy()

filtered_df["ai_risk_score"] = (
    filtered_df["transaction_amount"] / 300
    + filtered_df["investigation_hours"] * 4
)

filtered_df["ai_risk_score"] = (
    filtered_df["ai_risk_score"]
    .clip(0, 100)
    .round(0)
)

# =========================
# KPI CALCULATIONS
# =========================

total_alerts = len(filtered_df)

high_risk = len(
    filtered_df[filtered_df["risk_level"] == "High"]
)

total_amount = filtered_df["transaction_amount"].sum()

avg_hours = round(
    filtered_df["investigation_hours"].mean(),
    2
)

closure_rate = round(
    (
        len(filtered_df[filtered_df["status"] == "Closed"])
        / total_alerts
    ) * 100,
    1
)

avg_ai_score = round(
    filtered_df["ai_risk_score"].mean(),
    1
)

# =========================
# KPI CARDS
# =========================

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Total Alerts", total_alerts)

with col2:
    st.metric("High Risk Cases", high_risk)

with col3:
    st.metric(
        "Suspicious Amount",
        f"${total_amount:,.0f}"
    )

with col4:
    st.metric(
        "Avg Investigation Hours",
        avg_hours
    )

with col5:
    st.metric(
        "Closure Rate",
        f"{closure_rate}%"
    )

with col6:
    st.metric(
        "Avg AI Risk Score",
        avg_ai_score
    )

st.divider()

# =========================
# EXECUTIVE SUMMARY
# =========================

st.subheader("📌 Investigation Summary")

st.info(f"""
A total of {total_alerts} fraud alerts were analyzed.

High-risk investigations currently represent
{high_risk} active cases involving suspicious
transactions totaling ${total_amount:,.0f}.

Current operational analysis indicates elevated
financial crime exposure associated with
cross-border wire transfers and money laundering patterns.

Average AI risk exposure currently stands at
{avg_ai_score}/100.
""")

# =========================
# FUNNEL DATA
# =========================

funnel_data = pd.DataFrame({
    "Stage": [
        "Created",
        "Under Review",
        "Escalated",
        "Closed"
    ],
    "Count": [
        len(filtered_df[filtered_df["status"] == "Created"]),
        len(filtered_df[filtered_df["status"] == "Under Review"]),
        len(filtered_df[filtered_df["status"] == "Escalated"]),
        len(filtered_df[filtered_df["status"] == "Closed"])
    ]
})

# =========================
# FUNNEL CHART
# =========================

fig_funnel = px.funnel(
    funnel_data,
    x="Count",
    y="Stage",
    color="Stage",
    title="Fraud Investigation Funnel"
)

fig_funnel.update_layout(
    height=450,
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white"
)

# =========================
# FRAUD TYPE CHART
# =========================

fig_fraud = px.histogram(
    filtered_df,
    x="fraud_type",
    color="risk_level",
    title="Fraud Type Distribution",
    color_discrete_map={
        "High": "#FF4B4B",
        "Medium": "#FFA500",
        "Low": "#00C853"
    }
)

fig_fraud.update_layout(
    height=450,
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white"
)

# =========================
# TRANSACTION ANALYSIS
# =========================

fig_amount = px.scatter(
    filtered_df,
    x="transaction_amount",
    y="investigation_hours",
    color="risk_level",
    size="transaction_amount",
    hover_data=["fraud_type", "country"],
    title="Suspicious Transactions Analysis",
    color_discrete_map={
        "High": "#FF4B4B",
        "Medium": "#FFA500",
        "Low": "#00C853"
    }
)

fig_amount.update_layout(
    height=450,
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white"
)

# =========================
# AI RISK VISUALIZATION
# =========================

fig_risk_score = px.scatter(
    filtered_df,
    x="transaction_amount",
    y="ai_risk_score",
    color="risk_level",
    size="ai_risk_score",
    hover_data=["fraud_type", "country"],
    title="AI Risk Scoring Analysis",
    color_discrete_map={
        "High": "#FF4B4B",
        "Medium": "#FFA500",
        "Low": "#00C853"
    }
)

fig_risk_score.update_layout(
    height=450,
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font_color="white"
)

# =========================
# LAYOUT ROW 1
# =========================

col7, col8 = st.columns(2)

with col7:
    st.plotly_chart(
        fig_funnel,
        use_container_width=True
    )

with col8:
    st.plotly_chart(
        fig_fraud,
        use_container_width=True
    )

# =========================
# LAYOUT ROW 2
# =========================

col9, col10 = st.columns(2)

with col9:

    st.plotly_chart(
        fig_amount,
        use_container_width=True
    )

    st.plotly_chart(
        fig_risk_score,
        use_container_width=True
    )

with col10:

    st.subheader("🚨 Suspicious Activity Records")

    display_df = filtered_df[
        [
            "alert_id",
            "status",
            "risk_level",
            "transaction_amount",
            "ai_risk_score",
            "country",
            "investigation_hours",
            "fraud_type"
        ]
    ]

    styled_df = display_df.style.highlight_max(
        subset=["transaction_amount"],
        color="darkred"
    )

    st.dataframe(
        styled_df,
        use_container_width=True
    )

# =========================
# DOWNLOAD REPORT
# =========================

st.download_button(
    label="📥 Download Investigation Report",
    data=filtered_df.to_csv(index=False),
    file_name="fraud_investigation_report.csv",
    mime="text/csv"
)

# =========================
# FOOTER
# =========================

st.markdown("""
---
© 2026 Financial Crime Intelligence Center  
AI-Powered Fraud Detection & Investigation Analytics Platform
""")