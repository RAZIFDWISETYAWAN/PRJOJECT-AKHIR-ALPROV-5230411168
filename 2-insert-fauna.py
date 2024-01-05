# Import Module
import sqlite3

# Koneksi Database
koneksi = sqlite3.connect('database_fauna.db')

# INSERT DATA KE TABEL
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Harimau Jawa', 'Mamalia', 'Jawa', '40', '2019')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Kukus Beruang', 'Mamalia', 'Sulawesi', '30', '2021')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Beruang Madu', 'Mamalia', 'Sumatera', '1000', '2020')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Pesut Mahakam', 'Mamalia', 'Kalimantan', '100', '2021')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Burung Maleo', 'Burung', 'Sulawesi', '7000', '2023')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Macan Dahan', 'Mamalia', 'Sumatera', '400', '2020')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Kancil', 'Mamalia', 'Jawa', '60', '2022')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Gajah Kalimantan', 'Mamalia', 'Kalimantan', '1500', '2021')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Elang Jawa', 'Burung', 'Jawa', '200', '2021')
               ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jumlah_sekarang, tahun_ditemukan)
               VALUES('Katak Borneo', 'Amfibi', 'Kalimantan', '2000', '2023')
               ''')

koneksi.commit()
koneksi.close()