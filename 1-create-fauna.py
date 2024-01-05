# import module
import sqlite3

# Buat connection db
koneksi = sqlite3.connect('database_fauna.db')

# Create table baru
koneksi.execute(''' 
             CREATE TABLE FAUNA(
                 id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                 nama_fauna VARCHAR(50),
                 jenis VARCHAR(50),
                 asal VARCHAR(50),
                 jumlah_sekarang INT(10),
                 tahun_ditemukan INT(10)
             )
             
             ''')
# BREAK
koneksi.close()