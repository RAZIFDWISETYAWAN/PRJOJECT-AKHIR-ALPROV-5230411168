import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

id_fauna = 10
Asal_baru = "Kalimantan timur" 

kursor.execute(f"UPDATE Fauna SET asal = ? WHERE id_fauna = ? ", (Asal_baru, id_fauna,))
koneksi.commit()

print("DATA HEWAN INDONESIA 2023")
if kursor.rowcount > 0:
    print(f"Data Pesut mahakam Dengan ID {id_fauna} Berhasil Di Ubah!")
else:
    print(f"tidak ada data FAUNA dengan id {id_fauna}")

koneksi.close()