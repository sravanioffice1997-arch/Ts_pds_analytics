import streamlit as st
import pandas as pd

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="Shop Search",
    layout="wide"
)

st.title("🔍 FPS Shop Search & Benchmarking")

st.markdown("""
Enter an FPS Shop Number to compare its performance
against the average performance of similar shops in its cluster.
""")

# ----------------------------------
# LOAD DATA
# ----------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/pds_clustered.csv")

df = load_data()

# ----------------------------------
# SHOP SEARCH
# ----------------------------------
shop_no = st.text_input(
    "Enter Shop Number"
)

# ----------------------------------
# SEARCH LOGIC
# ----------------------------------
if shop_no:

    shop_data = df[
        df["shopno"].astype(str) == shop_no
    ]

    if shop_data.empty:

        st.error("Shop Number not found.")

    else:

        shop = shop_data.iloc[0]

        st.success("Shop Found")

        # ----------------------------------
        # SHOP DETAILS
        # ----------------------------------
        st.subheader("Shop Details")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Shop No",
            str(shop["shopno"])
        )

        col2.metric(
            "District",
            shop["distname"]
        )

        col3.metric(
            "Cluster",
            shop["cluster_name"]
        )

        # ----------------------------------
        # SHOP METRICS
        # ----------------------------------
        st.subheader("Shop Performance")

        metrics = [
            "nooftrans",
            "utilization_ratio",
            "portability_ratio",
            "rice_total",
            "total_commodity"
        ]

        # Cluster Average
        cluster_avg = (
            df[
                df["cluster"] == shop["cluster"]
            ][metrics]
            .mean()
        )

        # Shop Values
        shop_values = shop[metrics]

        # Comparison Table
        comparison_df = pd.DataFrame({
            "Metric": [
                "Transactions",
                "Utilization Ratio",
                "Portability Ratio",
                "Rice Distribution",
                "Total Commodity"
            ],
            "Shop Value": shop_values.values,
            "Cluster Average": cluster_avg.values
        })

        comparison_df["Difference"] = (
            comparison_df["Shop Value"]
            - comparison_df["Cluster Average"]
        )

        st.dataframe(
            comparison_df,
            use_container_width=True
        )

        # ----------------------------------
        # PERFORMANCE SUMMARY
        # ----------------------------------
        st.subheader("Performance Summary")

        above_avg = 0

        for metric in metrics:

            if shop[metric] > cluster_avg[metric]:
                above_avg += 1

        st.write(
            f"This shop performs above its cluster average in "
            f"**{above_avg} out of {len(metrics)} metrics.**"
        )

        # ----------------------------------
        # RAW DATA
        # ----------------------------------
        with st.expander("View Full Shop Record"):
            st.dataframe(
                shop_data,
                use_container_width=True
            )