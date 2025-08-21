import pandas as pd
from sqlalchemy import create_engine

def save_to_csv(df: pd.DataFrame, filename="goods.csv") -> None:
    """Menyimpan DataFrame ke file CSV lokal."""
    df.to_csv(filename, index=False)
    print(f"Data berhasil disimpan ke {filename}")

def save_to_postgresql(df: pd.DataFrame, table_name='goods') -> None:
    """Menyimpan DataFrame ke database PostgreSQL."""

    try:
        # Konfigurasi koneksi database (ubah sesuai kebutuhanmu)
        username = 'postgres'
        password = '77apaya'
        host = 'localhost'
        port = '5432'
        database = 'etldb'

        # Buat koneksi engine SQLAlchemy
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

        # Simpan DataFrame ke tabel PostgreSQL (replace = ganti tabel jika sudah ada)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data berhasil disimpan ke PostgreSQL, tabel: '{table_name}'")

    except Exception as error:
        print(f"Gagal menyimpan data ke PostgreSQL: {error}")