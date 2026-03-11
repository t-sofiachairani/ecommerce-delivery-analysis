import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="E-Commerce Delivery Analysis",
    page_icon="📦",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================
@st.cache_data
def load_data():

    BASE_DIR = Path(__file__).resolve().parent
    DATA_PATH = BASE_DIR / "final_dataset.csv"

    df = pd.read_csv(DATA_PATH)

    return df


df = load_data()

# =====================================
# SIDEBAR FILTER
# =====================================
with st.sidebar:

    st.title("Profil Analis")

    st.write("**Nama:** T. Sofia Chairani")
    st.write("**Email:** tsofiachairani@gmail.com")
    st.write("**ID Dicoding:** t-sofiachairani")

    st.markdown("---")

    st.subheader("Filter Data")

    # Filter Freight Cluster
    freight_filter = st.multiselect(
        "Freight Cluster",
        options=df["freight_cluster"].unique(),
        default=df["freight_cluster"].unique()
    )

    # Filter Volume Cluster
    volume_filter = st.multiselect(
        "Volume Cluster",
        options=df["volume_cluster"].unique(),
        default=df["volume_cluster"].unique()
    )

    # Slider Freight Value
    freight_range = st.slider(
        "Rentang Freight Value",
        int(df["freight_value"].min()),
        int(df["freight_value"].max()),
        (
            int(df["freight_value"].min()),
            int(df["freight_value"].max())
        )
    )

    # Slider Product Weight
    weight_range = st.slider(
        "Rentang Berat Produk (gram)",
        int(df["product_weight_g"].min()),
        int(df["product_weight_g"].max()),
        (
            int(df["product_weight_g"].min()),
            int(df["product_weight_g"].max())
        )
    )

# =====================================
# APPLY FILTER
# =====================================
filtered_df = df[
    (df["freight_cluster"].isin(freight_filter)) &
    (df["volume_cluster"].isin(volume_filter)) &
    (df["freight_value"].between(freight_range[0], freight_range[1])) &
    (df["product_weight_g"].between(weight_range[0], weight_range[1]))
]

# =====================================
# HEADER
# =====================================
st.title("📦 E-Commerce Delivery Analysis Dashboard")

st.write(
"""
Dashboard ini digunakan untuk menganalisis hubungan antara
dimensi produk, biaya pengiriman, dan waktu pengiriman
pada transaksi e-commerce.
"""
)

# =====================================
# KPI METRICS
# =====================================
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Transaksi",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Average Delivery Time",
    f"{filtered_df['delivery_time'].mean():.1f} hari"
)

col3.metric(
    "Average Freight Cost",
    f"{filtered_df['freight_value'].mean():.2f}"
)

st.divider()

# =====================================
# TABS
# =====================================
tab1, tab2, tab3 = st.tabs([
    "Dimensi Produk",
    "Biaya Pengiriman",
    "Clustering Analysis"
])

# =====================================
# TAB 1
# =====================================
with tab1:

    st.subheader("Pengaruh Dimensi Produk terhadap Waktu Pengiriman")

    fig, axes = plt.subplots(2,2, figsize=(12,8))

    sns.scatterplot(
        x="product_weight_g",
        y="delivery_time",
        data=filtered_df,
        alpha=0.3,
        ax=axes[0,0]
    )
    axes[0,0].set_title("Weight vs Delivery Time")

    sns.scatterplot(
        x="product_length_cm",
        y="delivery_time",
        data=filtered_df,
        alpha=0.3,
        ax=axes[0,1]
    )
    axes[0,1].set_title("Length vs Delivery Time")

    sns.scatterplot(
        x="product_height_cm",
        y="delivery_time",
        data=filtered_df,
        alpha=0.3,
        ax=axes[1,0]
    )
    axes[1,0].set_title("Height vs Delivery Time")

    sns.scatterplot(
        x="product_width_cm",
        y="delivery_time",
        data=filtered_df,
        alpha=0.3,
        ax=axes[1,1]
    )
    axes[1,1].set_title("Width vs Delivery Time")

    plt.tight_layout()

    st.pyplot(fig)

# =====================================
# TAB 2
# =====================================
with tab2:

    st.subheader("Pengaruh Biaya Pengiriman terhadap Waktu Pengiriman")

    fig, ax = plt.subplots()

    sns.scatterplot(
        x="freight_value",
        y="delivery_time",
        data=filtered_df,
        alpha=0.3,
        ax=ax
    )

    ax.set_xlabel("Freight Value")
    ax.set_ylabel("Delivery Time (days)")

    st.pyplot(fig)

# =====================================
# TAB 3
# =====================================
with tab3:

    st.subheader("Clustering Analysis")

    colA, colB = st.columns(2)

    with colA:

        st.write("Average Delivery Time by Freight Cluster")

        freight_avg = filtered_df.groupby("freight_cluster")["delivery_time"].mean()

        fig, ax = plt.subplots()
        freight_avg.plot(kind="bar", ax=ax)

        st.pyplot(fig)

    with colB:

        st.write("Average Delivery Time by Volume Cluster")

        volume_avg = filtered_df.groupby("volume_cluster")["delivery_time"].mean()

        fig, ax = plt.subplots()
        volume_avg.plot(kind="bar", ax=ax)

        st.pyplot(fig)

# =====================================
# DATA PREVIEW
# =====================================
st.divider()

st.subheader("Dataset Preview")

st.dataframe(filtered_df.head(50))