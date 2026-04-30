import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur tema seaborn
sns.set_theme(style='darkgrid')

# Load Data
day_df = pd.read_csv("dashboard/df_day_clean.csv")
hour_df = pd.read_csv("dashboard/df_hour_clean.csv")

# Pastikan kolom tanggal bertipe datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Membuat label cuaca yang lebih mudah dibaca
weather_labels = {1: 'Clear', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Ice'}
day_df['weathersit_label'] = day_df['weathersit'].map(weather_labels)

# Menyiapkan rentang tanggal untuk filter
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    st.header("Filter Data")
    # 1. Filter Tanggal
    date_range = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
    # Menghindari error saat user baru memilih 1 tanggal
    if len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = date_range[0]
        end_date = date_range[0] # Jadikan start_date dan end_date sama sementara
    
    # 2. Filter Cuaca (Selectbox dengan All Weathers)
    weather_options = ["Semua Cuaca", "Clear", "Mist/Cloudy", "Light Snow/Rain", "Heavy Rain/Ice"]
    selected_weather = st.selectbox("Kondisi Cuaca:", weather_options)

# --- FILTERING DATA ---
# Filter berdasarkan tanggal
main_day_df = day_df[(day_df["dteday"] >= str(start_date)) & (day_df["dteday"] <= str(end_date))]
main_hour_df = hour_df[(hour_df["dteday"] >= str(start_date)) & (hour_df["dteday"] <= str(end_date))]

# Filter berdasarkan cuaca (jika tidak memilih "Semua Cuaca")
if selected_weather != "Semua Cuaca":
    main_day_df = main_day_df[main_day_df['weathersit_label'] == selected_weather]

# --- MAIN PAGE ---
st.title('🚴‍♂️ Bike Sharing Data Dashboard')
st.markdown("Dashboard ini menampilkan visualisasi data penyewaan sepeda berdasarkan rentang waktu dan kondisi cuaca yang dipilih.")

# --- VISUALISASI 1: Pengaruh Cuaca ---
st.subheader('Rata-rata Penyewaan Sepeda Berdasarkan Cuaca')
if not main_day_df.empty:
    weather_rentals = main_day_df.groupby('weathersit_label')['cnt'].mean().reset_index()
    
    # Ukuran diperkecil (10, 5) agar nyaman dilihat
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.barplot(x='weathersit_label', y='cnt', data=weather_rentals, palette='viridis', ax=ax1)
    ax1.set_xlabel('Kondisi Cuaca')
    ax1.set_ylabel('Rata-rata Jumlah Penyewaan')
    st.pyplot(fig1, use_container_width=True)
else:
    st.warning("Data tidak tersedia untuk filter yang dipilih.")

# --- VISUALISASI 2: Pola Jam ---
st.subheader('Pola Penyewaan Sepeda per Jam (Hari Kerja vs Akhir Pekan)')
if not main_hour_df.empty:
    hourly_rentals = main_hour_df.groupby(['workingday', 'hr'])['cnt'].mean().reset_index()
    hourly_rentals['workingday'] = hourly_rentals['workingday'].map({0: 'Akhir Pekan/Libur', 1: 'Hari Kerja'})
    
    # Ukuran diperkecil (10, 5)
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='hr', y='cnt', hue='workingday', data=hourly_rentals, palette='Set1', marker='o', ax=ax2)
    ax2.set_xlabel('Jam (0-23)')
    ax2.set_ylabel('Rata-rata Jumlah Penyewaan')
    ax2.set_xticks(range(0, 24))
    ax2.grid(True, alpha=0.3)
    ax2.legend(title='Tipe Hari')
    st.pyplot(fig2, use_container_width=True)
else:
    st.warning("Data tidak tersedia untuk filter yang dipilih.")
