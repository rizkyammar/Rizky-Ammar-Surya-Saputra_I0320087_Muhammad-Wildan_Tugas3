#Membuat Dictionary

print("Membuat Dictionary")
dict = {'Nama': 'Rizky Ammar Surya Saputra', 'Hobby': 'Olahraga, Nonton Film, Running', 'Sosial Media': 'Instagram : @ammaar418, Line : @rizkyammar123, WhatsApp : 082218637951', 'Lagu Kesukaan': 'Pamungkas : Tobe bone, Fiersa Besari : Celengan Rindu', 'Makanan Favorit': 'Nasi Goreng, Telor Dadar, Mie Goreng, Martabak, Roti Bakar'}
print(dict)

#Mengubah Salah Satu Hobby dan Sosisal Media
print("Mengubah Salah Satu Isi Hobby dan Sosial Media")
dict['Hobby'][1] = 'Renang'
dict['Sosial Media'][2] = 'Gmail : rizkyammar123@gmail.com'
print(dict['Hobby'])
print(dict['Sosial Media'])

#Menghapus Makanan Favorit
print("Menghapus Makanan Favorit")
print("Makanan sebelum dihapus: ", dict['Makanan Favorit'])
del dict['Makanan Favorit'][0]
del dict['Makanan Favorit'][2]
print("Makanan Favorit Setelah Dihapus: ", dict['Makanan Favorit'])

#Menambahkan Satu Hobby
print("Hobby Sebelum ditambah: ", dict['Hobby'])
dict['Hobby'].append('Bermain Catur')
print("Hobby setelah ditambah")
print(dict['Hobby'])
