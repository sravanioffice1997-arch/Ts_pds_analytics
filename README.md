# Telangana Public Distribution System (PDS) Analytics

## Multi-Dimensional Fair Price Shop (FPS) Performance Clustering and Anomaly Profiling

---

# Project Overview

The **Telangana Public Distribution System (PDS)** distributes essential commodities through Fair Price Shops (FPS) across the state. This project applies **Data Analytics, Exploratory Data Analysis (EDA), Machine Learning, and Geospatial Visualization** to analyze FPS performance, beneficiary utilization, commodity distribution, portability adoption, clustering, and anomaly detection.

The project integrates **Transactions**, **Card Status**, and **FPS Location** datasets from **2023–2025** to generate operational insights and build an interactive Streamlit dashboard.

---

# Project Objectives

* Analyze Fair Price Shop operational performance.
* Study portability ("Other Shop Transactions") trends.
* Examine the relationship between beneficiary entitlement and actual transactions.
* Analyze district-wise commodity distribution.
* Segment FPS shops using Machine Learning clustering.
* Identify anomalous shops with unusual operational behavior.
* Visualize shop clusters on an interactive geospatial map.

---

# Dataset

* **Transactions Data (2023–2025):** 499,648 records
* **Card Status Data (2023–2025):** 517,516 records
* **FPS Locations:** 17,434 records
* **Unique Fair Price Shops:** 17,491
* **Coverage:** 33 Telangana Districts

The datasets were merged using:

* `shopNo`
* `distCode`
* `month`
* `year`

to create a unified analytical dataset.

---

# Data Preprocessing

* Merged 29 Transaction files into a master dataset.
* Merged 30 Card Status files into a master dataset.
* Performed Triple Join with FPS Location data.
* Removed duplicate shop records.
* Removed unnecessary columns.
* Handled missing values.
* Filled missing coordinates using median values.
* Validated district and office information.

---

# Exploratory Data Analysis (EDA)

The analysis included:

* Trend analysis of portability transactions (2023–2025)
* Correlation between Total Ration Cards (`totalRcs`) and Transactions (`noOfTrans`)
* Rice and Wheat distribution using histograms and boxplots
* District-wise commodity analysis
* Monthly seasonality analysis
* Heatmap visualization for seasonal transaction trends

---

# Feature Engineering

The following analytical features were created:

* Utilization Ratio
* Portability Ratio
* Total Rice Distribution
* Rice–Wheat Ratio
* Total Commodity Distribution
* Transactions per Card
* Transaction Volatility

---

# Machine Learning

## Feature Scaling

* StandardScaler

## Dimensionality Reduction

* Principal Component Analysis (PCA)

## Clustering

Algorithm Used:

* **K-Means Clustering**
* **Agglomerative Clustering**

Features Used:

* `noOfTrans`
* `utilization_ratio`
* `portability_ratio`
* `totalRice`
* `total_commodity`

The optimal clustering solution was evaluated using the **Silhouette Score**, resulting in **2 operational clusters** representing Standard Activity FPS Shops and High-Demand FPS Shops.

---

# Cluster Profiling

The clustering model segmented FPS shops into:

| Cluster   | Description                 |
| --------- | --------------------------- |
| Cluster 0 | Standard Activity FPS Shops |
| Cluster 1 | High-Demand FPS Shops       |

District-wise cluster distribution was analyzed to identify high-demand operational regions.

---

# Anomaly Detection

Algorithm Used:

* **Isolation Forest**

Highlights:

* Detected approximately **2% anomalous shops** using contamination-based anomaly detection.
* Generated anomaly scores for every FPS.
* Identified districts with higher concentrations of anomalous shop behavior.

---

# Streamlit Dashboard

The interactive dashboard includes:

* District-wise filtering
* KPI Cards

  * Total Shops
  * Total Transactions
  * Total Ration Cards
  * Total Anomalies
* Cluster Distribution
* Portability Trend Analysis
* Interactive Geospatial Map
* Shop Search
* Cluster Details
* Anomaly Profiling

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn
* Folium
* Streamlit

---

# Project Structure

```text
Ts_pds_analytics/
│
├── app.py
├── TS_govt_Ration_updated.ipynb
├── requirements.txt
├── README.md
├── master_df.csv
├── final_clustered_dataset.csv
│
├── Transactions/
├── Card_Status/
├── fps_locations.csv
│
└── images/
```

---

# Key Findings

* Portability ("Other Shop Transactions") showed an increasing trend from **2023 to 2025**.
* A strong positive correlation was observed between **Total Ration Cards** and **Number of Transactions**.
* Rice is the dominant commodity distributed across Telangana.
* K-Means clustering successfully identified two distinct operational categories of Fair Price Shops.
* Isolation Forest effectively detected anomalous FPS shops with unusual operational behavior.
* Urban districts exhibited comparatively higher transaction volumes and portability activity.

---

# Conclusion

This project demonstrates how Data Analytics and Machine Learning can be applied to evaluate the operational efficiency of Telangana's Public Distribution System. Through clustering, anomaly detection, geospatial visualization, and interactive dashboards, the project provides actionable insights into FPS performance, commodity distribution, beneficiary utilization, and portability adoption, supporting more informed decision-making for the Public Distribution System.

---

# Author

**Sravani**

GitHub Repository:

https://github.com/sravanioffice1997-arch/Ts_pds_analytics
