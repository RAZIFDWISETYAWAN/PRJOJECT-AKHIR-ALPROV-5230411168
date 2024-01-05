import sqlite3
hewan = sqlite3.connect('database_fauna.db')
kursor = hewan.cursor()
def tampilkan_data_sebelum():
    kursor.execute("SELECT * FROM FAUNA")
    data_sebelum = kursor.fetchall()

    print("Data sebelum Pengahapusan:")
    for row in data_sebelum:
        print(row)

    #hewan.close()

def tampilkan_data_sesudah():
    kursor.execute("DELETE FROM FAUNA WHERE asal = 'Kalimantan' ")
    
    kursor.execute("SELECT * FROM FAUNA")
    data_sesudah = kursor.fetchall()

    print("Data Sesudah Penghapusan:")
    for row in data_sesudah:
        print(row)

    hewan.close()

tampilkan_data_sebelum()

tampilkan_data_sesudah()