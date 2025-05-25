#  untuk mengecek apakah semua elemen dalam tuple sama
def cek(tup):
    # tuple diubah jadi set 
    # Jika semua elemen sama, maka panjang set hanya 1
    return len(set(tup)) == 1

# Contoh tuple yg sma
tA = (90, 90, 90, 90)#output: true(karean semua elemen sama)
tB = (90, 80, 82, 90)#output: false(elemen ada yg beda)
print(cek(tA))
print(cek(tB))
