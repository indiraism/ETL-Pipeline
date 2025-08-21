# Basic Data Processing

Sebanyak 50 halaman data diekstraksi, dibersihkan, dan disimpan ke berbagai platform penyimpanan.

## Directory Layout

Suggested:

```
.
├── main.py
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── goods.csv
└── README.md
```


## Feature

- _Extract_: Mengambil informasi produk dari _website_ dengan memanfaatkan pustaka _requests_ dan 'BeautifulSoup' untuk _scraping_ data.
- _Transform_: Melakukan pembersihan dan penataan ulang data menggunakan pandas, agar siap digunakan lebih lanjut.
- _Load_: Menyimpan data yang telah diproses ke dalam format CSV (goods.csv) dan juga mengunggahnya ke basis data PostgreSQL.


# How to Run the Project

🛠 Menjalankan Skrip _ETL Pipeline_
- Pastikan semua _library_ yang dibutuhkan seperti _requests, beautifulsoup4, pandas, dan psycopg2_ sudah terpasang di lingkungan Python Anda.
- Buka terminal di folder proyek, lalu jalankan perintah:

```bash
python main.py
```

✅ Menjalankan _Unit Test_
- Pastikan modul _unittest_ tersedia (modul ini biasanya sudah termasuk dalam instalasi Python standar).
- Untuk menjalankan semua test, gunakan perintah berikut di terminal:

```bash
python -m unittest discover tests
```

📊 Menjalankan _Test Coverage_
- Pastikan Anda telah menginstal _package coverage_ dengan perintah:

```bash
pip install coverage
```

- Jalankan pengujian dan lihat laporan cakupan kode dengan perintah:

```bash
coverage run -m unittest discover tests
coverage report -m
```


## PostgreSQL Database Configuration

Ensure that the PostgreSQL credentials and connection details used in the `save_to_postgresql()` function (located in `utils/load.py`) are properly configured for your local development environment.

```python
username = 'postgres'
password = '77apaya'
host = 'localhost'
port = '5432'
database = 'etldb'
```
