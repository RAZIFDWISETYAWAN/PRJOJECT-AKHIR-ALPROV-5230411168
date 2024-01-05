import sqlite3
hewan = sqlite3.connect('database_fauna.db')
kursor = hewan.cursor()

id_fauna = 10
jml_Sekarang_baru = 650

kursor.execute(f"UPDATE FAUNA SET jumlah_sekarang = {jml_Sekarang_baru} WHERE id_fauna = {id_fauna}")
hewan.commit()

print("DATA HEWAN INDONESIA 2023")
if kursor.rowcount > 0:
    print(f"Data KATAK BORNOE Dengan ID {id_fauna} Berhasil Di Ubah!")
else:
    print(f"tidak ada data FAUNA dengan id {id_fauna}")

hewan.close()
