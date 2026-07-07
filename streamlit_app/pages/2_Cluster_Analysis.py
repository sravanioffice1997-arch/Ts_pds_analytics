import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("Cluster Analysis")

cluster_counts = (
    df['cluster_name']
    .value_counts()
)

fig = px.bar(
    cluster_counts,
    title="Cluster Distribution"
)

st.plotly_chart(fig)
