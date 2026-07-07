import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Geospatial Cluster Map",
    layout="wide"
)

st.title("🗺 Telangana PDS Geospatial Cluster Map")


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/pds_clustered.csv")

df = load_data()

# --------------------------------------------------
# REMOVE MISSING COORDINATES
# --------------------------------------------------
map_df = df.dropna(
    subset=["latitude", "longitude"]
)

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("Filters")

districts = sorted(
    map_df["distname"].dropna().unique()
)

selected_district = st.sidebar.selectbox(
    "Select District",
    ["All Districts"] + districts
)

if selected_district != "All Districts":
    map_df = map_df[
        map_df["distname"] == selected_district
    ]

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Shops",
    len(map_df)
)

col2.metric(
    "Districts",
    map_df["distname"].nunique()
)

col3.metric(
    "Clusters",
    map_df["cluster_name"].nunique()
)

# --------------------------------------------------
# MAP
# --------------------------------------------------
fig = px.scatter_mapbox(
    map_df,
    lat="latitude",
    lon="longitude",
    color="cluster_name",
    hover_name="shopno",
    hover_data={
        "distname": True,
        "nooftrans": True,
        "utilization_ratio": True,
        "portability_ratio": True,
        "cluster_name": True,
        "latitude": False,
        "longitude": False
    },
    zoom=6,
    height=500,
    color_discrete_map={
        "Standard Activity FPS Shops": "green",
        "High-Demand FPS Shops": "red"
    }
)

fig.update_layout(
    mapbox_style="carto-positron",
    margin=dict(
        l=0,
        r=0,
        t=0,
        b=0
    ),
    legend_title_text="Cluster"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# DEBUG SECTION
# --------------------------------------------------
with st.expander("Cluster Distribution "):
    st.write(
        map_df["cluster_name"].value_counts()
    )

# --------------------------------------------------
# SAMPLE DATA
# --------------------------------------------------
with st.expander("View Sample Records"):
    st.dataframe(
        map_df[
            [
                "shopno",
                "distname",
                "cluster_name",
                "nooftrans",
                "utilization_ratio",
                "portability_ratio"
            ]
        ].head(20)
    )