#List 10 Nama Teman
list = ['Tito', 'Sony', 'Yeario', 'Rizky', 'Alvin', 'Ryan', 'Rahmat', 'Vincentius', 'William', 'Rizal']

print(list)
print("Isi list indeks 4,6,dan  7: ", list[4], list[6], list[7])

#Ganti nama teman di list 3,5,9
print("List 3,5,9 sebelum diganti: ", list[3], list[5], list[9])

list[3] = 'Anindra'
list[5] = 'Anderson'
list[9] = 'Adam'

print("List 3,5,9 setelah diganti: ", list[3], list[5], list[9])

#Menambahkan dua nama teman
print("List sebelum ditambah: ", list)
list.append('Surya')
list.append('Saputra')
print("List setelah ditambah: ", list)

#menampilkan panjang list
len(list)
print("Menampilkan panjang list: ", len(list))







