import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="E-Commerce Delivery Analysis",
    page_icon="📦",
    layout="wide"
)

# ==============================
# LOAD DATA
# ==============================
@st.cache_data
def load_data():
    df = pd.read_csv("final_dataset.csv")
    return df

df = load_data()

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:

    st.title("Profil Analis")

    st.write("**Nama:** T. Sofia Chairani")
    st.write("**Email:** tsofiachairani@gmail.com")
    st.write("**ID Dicoding:** t-sofiachairani")

    st.markdown("---")

    st.write(
        """
        Dashboard ini menampilkan analisis pengaruh dimensi produk
        dan biaya pengiriman terhadap waktu pengiriman
        pada transaksi e-commerce periode 2017-2018.
        """
    )

# ==============================
# HEADER
# ==============================
st.title("📦 E-Commerce Delivery Analysis Dashboard")

st.write(
"""
Dashboard ini digunakan untuk menganalisis hubungan antara
dimensi produk, biaya pengiriman, dan waktu pengiriman
pada transaksi e-commerce.
"""
)

# ==============================
# KPI
# ==============================
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Transaksi",
    f"{len(df):,}"
)

col2.metric(
    "Rata-rata Delivery Time",
    f"{df['delivery_time'].mean():.1f} hari"
)

col3.metric(
    "Rata-rata Freight Cost",
    f"{df['freight_value'].mean():.2f}"
)

st.divider()

# ==============================
# TABS
# ==============================
tab1, tab2, tab3 = st.tabs([
    "Dimensi Produk",
    "Biaya Pengiriman",
    "Clustering Analysis"
])

# ==============================
# TAB 1 : DIMENSI PRODUK
# ==============================
with tab1:

    st.subheader("Pengaruh Dimensi Produk terhadap Waktu Pengiriman")

    fig, axes = plt.subplots(2, 2, figsize=(12,8))

    sns.scatterplot(
        x="product_weight_g",
        y="delivery_time",
        data=df,
        alpha=0.3,
        ax=axes[0,0]
    )
    axes[0,0].set_title("Weight vs Delivery Time")

    sns.scatterplot(
        x="product_length_cm",
        y="delivery_time",
        data=df,
        alpha=0.3,
        ax=axes[0,1]
    )
    axes[0,1].set_title("Length vs Delivery Time")

    sns.scatterplot(
        x="product_height_cm",
        y="delivery_time",
        data=df,
        alpha=0.3,
        ax=axes[1,0]
    )
    axes[1,0].set_title("Height vs Delivery Time")

    sns.scatterplot(
        x="product_width_cm",
        y="delivery_time",
        data=df,
        alpha=0.3,
        ax=axes[1,1]
    )
    axes[1,1].set_title("Width vs Delivery Time")

    plt.tight_layout()

    st.pyplot(fig)

# ==============================
# TAB 2 : BIAYA PENGIRIMAN
# ==============================
with tab2:

    st.subheader("Pengaruh Biaya Pengiriman terhadap Waktu Pengiriman")

    fig, ax = plt.subplots()

    sns.scatterplot(
        x="freight_value",
        y="delivery_time",
        data=df,
        alpha=0.3,
        ax=ax
    )

    ax.set_xlabel("Freight Value")
    ax.set_ylabel("Delivery Time (days)")
    ax.set_title("Freight Value vs Delivery Time")

    st.pyplot(fig)

# ==============================
# TAB 3 : CLUSTERING
# ==============================
with tab3:

    st.subheader("Clustering Analysis")

    colA, colB = st.columns(2)

    # Freight Cluster
    with colA:

        st.write("Average Delivery Time by Freight Cluster")

        freight_avg = df.groupby("freight_cluster")["delivery_time"].mean()

        fig, ax = plt.subplots()

        freight_avg.plot(
            kind="bar",
            ax=ax
        )

        ax.set_ylabel("Average Delivery Time")

        st.pyplot(fig)

    # Volume Cluster
    with colB:

        st.write("Average Delivery Time by Volume Cluster")

        volume_avg = df.groupby("volume_cluster")["delivery_time"].mean()

        fig, ax = plt.subplots()

        volume_avg.plot(
            kind="bar",
            ax=ax
        )

        ax.set_ylabel("Average Delivery Time")

        st.pyplot(fig)

# ==============================
# DATA PREVIEW
# ==============================
st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head(50))

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.caption("Proyek Analisis Data - Dicoding")