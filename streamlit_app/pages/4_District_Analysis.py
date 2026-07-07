import streamlit as st
import pandas as pd

from utils.data_loader import load_data

df = load_data()

st.title("District Analysis")

district_cluster = pd.crosstab(
    df['distname'],
    df['cluster_name']
)

st.dataframe(
    district_cluster
)
