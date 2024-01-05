# import module
import sqlite3

# Koneksi Database
koneksi = sqlite3.connect("database_fauna.db")
kursor = koneksi.cursor()

# Ambil data berdasarkan rata rata gaji
kursor.execute("SELECT SUM(jumlah_sekarang) FROM FAUNA") # BISA PAKAI SUM (DENGAN AVG DIGANTI SUM)
jumlah_fauna = kursor.fetchone()[0] # Ambil data gaji jadikan baris baru dimulai dari indeks 0

print(f"Jumlah Total Hewan Langka Saat Ini Adalah: {jumlah_fauna}")

koneksi.close()