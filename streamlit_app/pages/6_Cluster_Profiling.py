import streamlit as st

from utils.data_loader import load_data

df = load_data()

st.title(
    "Cluster Profiling"
)

profile = (
    df.groupby('cluster_name')
    [
        [
            'nooftrans',
            'utilization_ratio',
           
            'rice_total',
            'total_commodity'
        ]
    ]
    .mean()
)

st.dataframe(profile)
