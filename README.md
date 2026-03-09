# bike-sharing


Analisis dataset transaksi e-commerce untuk memahami pengaruh **dimensi produk** dan **biaya pengiriman** terhadap **waktu pengiriman** menggunakan Python (Pandas, Seaborn) dan visualisasi interaktif dengan **Streamlit Dashboard**.

- Akses melalui: [E-Commerce Delivery Dashboard](https://ecommerce-delivery-analysis.streamlit.app/)

## Setup Environment - Anaconda

```text
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Fitur Utama

- **KPI Metrics:** Total transaksi, rata-rata waktu pengiriman dan rata-rata biaya pengiriman.
- **Analisis Dimensi Produk:** Visualisasi hubungan antara dimensi produk dengan waktu pengiriman.
- **Analisis Biaya Pengiriman:** Menganalisis pengaruh freight cost terhadap durasi pengiriman.
- **Segmentasi (Clustering):** Pengelompokan transaksi berdasarkan karakteristik.

## Struktur Folder

```text
.
├── dashboard/
│   ├── dashboard.py        # File utama dashboard Streamlit
│   └── final_dataset.csv   # Dataset hasil preprocessing
│
├── data/
│   ├── orders_dataset.csv
│   ├── order_items_dataset.csv
│   └── products_dataset.csv
│
├── notebook.ipynb          # Proses analisis data (EDA & data preparation)
├── README.md               # Dokumentasi proyek
└── requirements.txt        # Daftar library yang dibutuhkan
```

## Menjalankan Project

```bash
# Clone repository
git clone https://github.com/t-sofiachairani/ecommerce-delivery-analysis.git

# Masuk ke folder project
cd ecommerce-delivery-analysis

# Install dependencies
pip install -r requirements.txt

# Jalankan dashboard
streamlit run dashboard/dashboard.py
streamlit run dashboard.py
```
