file_name = input("Enter a file name: ")  # Meminta kita memasukkan nama file

try:
    with open(file_name, 'r') as file_handle:  # Mencoba membuka file
        hour_counts = dict()  # Membuat dictionary untuk menghitung jumlah jam

        for line in file_handle:  # Membaca setiap baris dalam file
            if line.startswith('From '):  # Memproses hanya baris yang diawali 'From '
                time = line.split()[5]  # Mengambil data waktu (jam:menit:detik)
                hour = time.split(':')[0]  # Mengambil bagian jam saja
                hour_counts[hour] = hour_counts.get(hour, 0) + 1  # Tambah hitungan jam ke dictionary

        for hour in sorted(hour_counts):  # Mengurutkan jam
            print(hour, hour_counts[hour])  # Cetak jam dan jumlah kemunculannya

except FileNotFoundError:  # Jika file tidak ditemukan Tampilkan pesan error
    print("File cannot be opened:", file_name)  

