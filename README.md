# Bike-Sharing Demand Analysis

> Proyek Analisis Data — Belajar Fundamental Analisis Data
> **Dicoding Indonesia**

---

## Deskripsi Proyek

Proyek ini merupakan analisis mendalam terhadap dataset **Capital Bikeshare** dari Washington D.C., sebuah sistem penyewaan sepeda publik yang beroperasi pada tahun **2011–2012**. Tujuan utama proyek ini adalah menjawab pertanyaan bisnis yang relevan melalui proses analisis data yang terstruktur, mulai dari pembersihan data, eksplorasi, visualisasi, hingga kesimpulan yang dapat dijadikan dasar pengambilan keputusan.

### Pertanyaan Bisnis yang Dijawab

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda harian?
2. Pada jam berapa permintaan penyewaan sepeda mencapai puncaknya, dan apakah polanya berbeda antara hari kerja dan akhir pekan?
3. Faktor lingkungan mana (suhu, kelembaban, kecepatan angin) yang paling berkorelasi dengan jumlah penyewaan?
4. Bagaimana tren pertumbuhan penggunaan sepeda dari tahun 2011 ke 2012 berdasarkan musim?
5. Pada kombinasi kondisi apa (musim, cuaca, jam) penyewaan berada di titik paling sepi?
6. Bagaimana profil pengguna berdasarkan kontribusi tipe penyewaan (kasual vs terdaftar)?

---

## Struktur Direktori

```
submission
├── dashboard/
│   ├── df_day_clean.csv     # Dataset utama yang sudah dibersihkan
│   ├── df_hour_clean.csv    # Dataset utama yang sudah dibersihkan
│   └── dashboard.py         # Aplikasi dashboard Streamlit
├── data/
│   ├── day.csv              # Dataset penyewaan harian (raw)
│   └── hour.csv             # Dataset penyewaan per jam (raw)
├── notebook.ipynb           # Notebook analisis lengkap
├── README.md                # Dokumentasi proyek (file ini)
├── requirements.txt         # Daftar dependensi Python
└── url.txt                  # Link dashboard online
```

---

## Tentang Dataset

Dataset berasal dari sistem **Capital Bikeshare** Washington D.C. dan berisi informasi penyewaan sepeda selama 2 tahun (2011–2012).

| File | Baris | Kolom | Deskripsi |
|------|-------|-------|-----------|
| `day.csv` | 731 | 16 | Agregat penyewaan harian |
| `hour.csv` | 17.379 | 17 | Agregat penyewaan per jam |

### Kamus Variabel

| Variabel | Tipe | Deskripsi |
|----------|------|-----------|
| `dteday` | date | Tanggal pencatatan |
| `season` | int | Musim: 1=Spring, 2=Summer, 3=Fall, 4=Winter |
| `yr` | int | Tahun: 0=2011, 1=2012 |
| `mnth` | int | Bulan: 1–12 |
| `hr` | int | Jam: 0–23 *(hanya di hour.csv)* |
| `holiday` | int | 1 jika hari libur nasional |
| `weekday` | int | Hari dalam seminggu: 0=Minggu s.d. 6=Sabtu |
| `workingday` | int | 1 jika hari kerja |
| `weathersit` | int | Kondisi cuaca: 1=Cerah, 2=Mendung, 3=Hujan Ringan |
| `temp` | float | Suhu ternormalisasi (×41 = °C) |
| `atemp` | float | Suhu terasa ternormalisasi (×50 = °C) |
| `hum` | float | Kelembaban ternormalisasi (×100 = %) |
| `windspeed` | float | Kecepatan angin ternormalisasi (×67 = kph) |
| `casual` | int | Jumlah penyewaan pengguna tidak terdaftar |
| `registered` | int | Jumlah penyewaan pengguna terdaftar |
| `cnt` | int | Total penyewaan (casual + registered) |

---

## Alur Analisis (dalam `notebook.ipynb`)

### 1. Data Wrangling
- **Gathering Data** — memuat `day.csv` dan `hour.csv`
- **Assessing Data** — memeriksa tipe data, missing values, duplikasi, outlier, dan statistik deskriptif
- **Cleaning Data** — konversi tipe data, mapping label kategorikal, dan denormalisasi nilai numerik ke satuan asli (°C, %, kph)

### 2. Exploratory Data Analysis (EDA)
- Distribusi dan statistik variabel target (`cnt`, `casual`, `registered`)
- Matriks korelasi antar variabel lingkungan dan penyewaan
- Analisis statistik per kondisi cuaca, musim, dan jam
- Profil komposisi pengguna kasual vs terdaftar

### 3. Visualization & Explanatory Analysis
Menjawab 6 pertanyaan bisnis dengan visualisasi yang informatif:
- Bar chart + Boxplot pengaruh cuaca terhadap penyewaan
- Area chart pola per jam (hari kerja vs akhir pekan)
- Scatter plot + regresi linier korelasi faktor lingkungan
- Grouped bar chart tren pertumbuhan 2011 vs 2012
- Heatmap kombinasi musim × cuaca dan jam × hari
- Stacked area chart profil tipe pengguna

### 4. Analisis Lanjutan
- Segmentasi 24 jam berdasarkan tingkat permintaan (Low/Medium/High Demand)
- Matriks korelasi lengkap semua variabel utama
- Tren bulanan time-series dengan area pertumbuhan 2011 vs 2012

### 5. Conclusion
Rangkuman temuan dan rekomendasi strategis berbasis data untuk optimalisasi operasional layanan bike-sharing.

---

## Temuan Utama

- **Cuaca** adalah faktor eksternal paling dominan — cuaca hujan ringan menurunkan penyewaan hingga **63%** dibandingkan cuaca cerah
- **Hari kerja** memiliki pola bimodal (puncak jam 08:00 dan 17:00–18:00) yang didominasi komuter terdaftar, sementara **akhir pekan** memiliki pola unimodal di siang hari
- **Suhu** adalah faktor lingkungan dengan korelasi positif terkuat (r ≈ +0.63) terhadap total penyewaan
- Semua musim mengalami pertumbuhan rata-rata **di atas 60%** dari 2011 ke 2012
- **Pengguna terdaftar** mendominasi ~81% dari total penyewaan dan menjadi penggerak utama permintaan

---
## Menjalankan Dashboard Streamlit secara Lokal

### 1. Persiapan Environment (Setup)
Sangat disarankan untuk menggunakan *virtual environment* agar dependensi proyek ini terisolasi dengan baik.
```bash
# Clone repository (jika menggunakan GitHub)
git clone [https://github.com/rianarifiya/BFAD_Riana-Shofiatul-Khoeriyah.git](https://github.com/rianarifiya/BFAD_Riana-Shofiatul-Khoeriyah.git)

# Masuk ke direktori proyek (pastikan menggunakan tanda kutip karena ada spasi)
cd "Submission_BFAD_Riana Shofiatul Khoeriyah"

# Buat virtual environment bernama 'venv'
python -m venv venv

# Aktifkan virtual environment
# Untuk pengguna Windows (Command Prompt / PowerShell):
venv\Scripts\activate
# Untuk pengguna Mac/Linux:
source venv/bin/activate

# Instalasi library
pip install -r requirements.txt

### Menjalankan Dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

# Atau, jika di Windows menggunakan PowerShell sering terjadi error:
# python -m streamlit run dashboard.py

Dashboard akan terbuka otomatis di browser pada `http://localhost:8501`

### Fitur Dashboard

| Tab | Konten |
|-----|--------|
| Tren & Musim | Grafik tren bulanan 2011 vs 2012 + bar chart per musim |
| Pola Per Jam | Area chart interaktif hari kerja vs akhir pekan + tabel jam tersibuk |
| Cuaca & Lingkungan | Bar chart kondisi cuaca + scatter plot korelasi + heatmap musim×cuaca |
| Segmentasi Pengguna | Pie chart proporsi + stacked area per jam + bar chart per hari |

> Semua visualisasi mendukung filter interaktif berdasarkan **Tahun**, **Musim**, dan **Kondisi Cuaca** melalui sidebar.

---

## Live Dashboard

**[https://rianarifiya-bikesharing.streamlit.app/](https://rianarifiya-bikesharing.streamlit.app/)**

---

## Library yang Digunakan

| Library | Versi | Kegunaan |
|---------|-------|---------|
| `pandas` | 2.3.3 | Manipulasi dan analisis data tabular |
| `numpy` | 1.26.4 | Komputasi numerik |
| `matplotlib` | 3.9.2 | Visualisasi data dasar |
| `seaborn` | 0.13.2 | Visualisasi statistik tingkat lanjut |
| `scipy` | 1.14.1 | Uji statistik dan regresi linier |
| `streamlit` | 1.55.0 | Framework dashboard interaktif |

---

## Profil Penulis

- **Nama:** Riana Shofiatul Khoeriyah
- **Email:** rianashofiatulkhoeriyah24@gmail.com
- **ID Dicoding:** riana_sk

---

## Sumber Data

Sumber: [Bike Sharing Dataset — Google Drive](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)
