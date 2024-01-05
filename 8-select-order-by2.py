# import module
import sqlite3

# Koneksi Database
koneksi = sqlite3.connect("database_fauna.db")

# Buat variable cursos untuk menampung data
kursor = koneksi.cursor()

# Select data from table
# Bintang(*) artinya menyeleksi semua isian table
kursor.execute("SELECT * FROM FAUNA FAUNA ORDER BY jumlah_sekarang DESC")
baris_tabel = kursor.fetchall()

# MEMBUAT FROM TABEL DENGAN METHOD FORMAT()
print("DATA FAUNA MAMALIA")
print("="*100)
print("{:<5}{:<20}{:20}{:<20}{:<20}{:<20}".format("ID", "Nama_Fauna", "Jenis", "Asal", "Jumlah_Sekarang", "Tahun_Ditemukan"))
print("-"*100)

# Tampilka Data Sesuai Format Tabel Dengan Perulangan
for baris in baris_tabel:
    print("{:<5}{:<20}{:20}{:<20}{:<20}{:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close