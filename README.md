# Speeend - Backend API Pengeluaran Harian

Speeend adalah aplikasi backend berbasis RESTful API yang dirancang untuk membantu pengelolaan data pengeluaran harian. Proyek ini dibangun untuk memenuhi tugas mata kuliah Komputasi Awan dengan fokus pada implementasi model layanan Platform as a Service (PaaS).

## Fitur Utama
- **Tambah Pengeluaran**: Mencatat jumlah, kategori, catatan, dan tanggal pengeluaran.
- **Daftar Pengeluaran**: Menampilkan seluruh riwayat pengeluaran yang tersimpan.
- **Ringkasan Kategori**: Menyajikan total pengeluaran secara keseluruhan dan ringkasan per kategori.
- **Health Check**: Endpoint untuk memantau status kesehatan dan kesiapan aplikasi.

## Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python 3.11
- **Framework**: Flask
- **Database**: SQLite (SQLAlchemy ORM)
- **Web Server**: Gunicorn
- **Infrastruktur**: AWS Elastic Beanstalk (PaaS)

## Struktur Endpoint
- `GET /` : Informasi dasar aplikasi.
- `GET /health` : Mengecek status aplikasi.
- `POST /expenses` : Menambahkan data pengeluaran baru (Format JSON).
- `GET /expenses` : Mengambil semua data pengeluaran.
- `GET /expenses/summary` : Melihat ringkasan total pengeluaran.
