# tuple dalam fungsi
def cetak_info(data):
    nama, umur = data
    print(f"{nama} berumur {umur} tahun")

cetak_info(("Rani", 20))



tuple1 = (1, 2, 3, "a", "b")
print(tuple1)  # Output: (1, 2, 3, 'a', 'b')

tuple2 = 4, 5, 6  #tuple tanpa kurung
print(tuple2)  # Output: (4, 5, 6)

tuple3=tuple('anggicute')
print(tuple3)#output :('a', 'n', 'g', 'g', 'i', 'c', 'u', 't', 'e')

tuple4=('a','n','g','g','i')
print(tuple4[0]) #output a
print(tuple4[2:5])#output ('g', 'g', 'i')

t1 = (0, 1, 2)
t2 = (3, 4, 5)

hasil = t1 > t2  # Membandingkan t1 dan t2
print(hasil)     # Output: False

kata = 'jimin pacar aku'
daftar_kata = kata.split()
urutan = sorted(daftar_kata, key=len, reverse=True)
print(urutan)# output: ['jimin', 'pacar', 'aku']


# Penugasan Tuple
# Contoh 1: Membongkar list ke variabel
kata = ['JIMIN', 'jungkok']
kata1, kata2 = kata
print(kata1)  # Output: JIMIN
print(kata2)  # Output: jungkok

# Contoh 2: Menukar nilai variabel
k1 = "bright"
k2 = "future"
k1, k2 = k2, k1  # Menukar nilai dengan tuple
print(k1)  # Output: future
print(k2)  # Output: bright

# Membagi alamat email menjadi username dan domain
email = 'anggrayni.layuk@ti.ukdw.ac.id'
username, domain = email.split('@')
print(username)  # Output: anggrayni.layuk
print(domain)   # Output: ti.ukdw.ac.id


# Dictionary data berbeda
nilai = {'Adit': 85, 'sopo': 92, 'jarwo': 78}

# Konversi ke list tuple
tuple = list(nilai.items())
print("Data awal:", tuple)
# Urutkan berdasarkan nama 
tuple.sort()
print("Urut nama A-Z:", tuple)
# Urutkan berdasarkan nilai
tuple.sort(key=lambda x: x[1], reverse=True)
print("Urut nilai tertinggi:", tuple)

#output:
# Data awal: [('Adit', 85), ('sopo', 92), ('jarwo', 78)]
# Urut nama A-Z: [('Adit', 85), ('jarwo', 78), ('sopo', 92)]
# Urut nilai tertinggi: [('sopo', 92), ('Adit', 85), ('jarwo', 78)]


# Dictionary dengan data 
data = {'x': 20, 'y': 25, 'z': 10}
# Membuat list tuple (nilai, key) 
result = []
for key, v in data.items():
    result.append((v, key))

print("Sebelum diurutkan:", result)
# Mengurutkan berdasarkan nilai
result.sort(reverse=True)
print("Setelah diurutkan:", result)
#output :
# Sebelum diurutkan: [(20, 'x'), (25, 'y'), (10, 'z')]
# Setelah diurutkan: [(25, 'y'), (20, 'x'), (10, 'z')]


import string
with open('as.txt', 'r') as file:
    text = file.read()

#menghilakan tanda baca dan ubah kehuruf kecil
translator = str.maketrans('', '', string.punctuation)
hapus_kata = text.translate(translator).lower()

# perulangan Hitung frekuensi kata
word_counts = dict()
for word in hapus_kata.split():
    word_counts[word] = word_counts.get(word, 0) + 1

# Ubah ke list of tuple, lalu urutkan berdasarkan jumlah (frekuensi)
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
# Cetak 10 kata paling sering muncul
for word, count in sorted_words[:10]:
    print(word, count)


last = 'layuk'
first = 'anggrayni'
number = '087886522738'

directory = dict()
# Menggunakan tuple (last, first) sebagai key
directory[last, first] = number
# Menampilkan isi dictionary
for last, first in directory:
    print(first, last, directory[last, first])

#output: anggrayni layuk 087886522738