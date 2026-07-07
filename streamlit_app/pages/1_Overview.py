import streamlit as st
from utils.data_loader import load_data

df = load_data()

st.title("Overview")

col1,col2,col3 = st.columns(3)

col1.metric(
    "Total Shops",
    df['shopno'].nunique()
)

col2.metric(
    "Total Transactions",
    int(df['nooftrans'].sum())
)

col3.metric(
    "Total Ration Cards",
    int(df['totalrcs'].sum())
)
