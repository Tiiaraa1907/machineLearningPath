# len()
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))
 
contoh_set = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_set)
print(len(contoh_set))
 
contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))

# min() dan max()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# count
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# penggabungan dan replikasi
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)

learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2
print(replikasi)

tujuh = [7]*7
print(len(tujuh))
print(tujuh)

# range()
for i in range(5):
    print(i)

# in and not in
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# insert value in multiple variable
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]

# sort() : for arrange alphabet or number
angka = [100, 1000, 500, 200, 5]
angka.sort()
print(angka)

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

# untuk urutan terbalik
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)
