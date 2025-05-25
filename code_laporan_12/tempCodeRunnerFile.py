data = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')

# jadikan nama, NIM, dan alamat dari tuple
nama = data[0]
nim = data[1]
alamat = data[2]

# Ubah NIM menjadi tuple per karakter
nim_tup = tuple(nim)

# Ambil nama depan dari nama lengkap
nama_depan = nama.split()[0]

# Ubah nama depan (tanpa huruf pertama) menjadi tuple per huruf
nama_depan_tup = tuple(nama_depan[1:])

# Balik urutan nama (jadi: Nendya Bhakti Matahari) lalu ubah jadi tuple
nama_terbalik_tup = tuple(nama.split()[::-1])

# Cetak semua hasil
print(f"Data: {data}\n")
print(f"NIM : {nim}")
print(f"NAMA : {nama}")
print(f"ALAMAT : {alamat}\n")
print(f"NIM: {nim_tup}\n")
print(f"NAMA DEPAN: {nama_depan_tup}\n")
print(f"NAMA TERBALIK: {nama_terbalik_tup}\n")
