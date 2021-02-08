# JENIS-JENIS LIST PADA PYTHON:
# 1. LIST
# 2. TUPLE
# 3. SET
# 4. DICTIONARY

# x = [5,10,15,20,25,30,35,40]
# print(x[5])
# print(x[-1])
# print(x[3:5])
# print(x[:5])
# print(x[-3:])
# print(x[1:7:2])

# # CARA MENGGANTI ISI ARRAY
# x = [1,2,3]
# x[2]=4
# print (x)

# CARA MENAMBAH ISI ARRAY

# x = [1,2,3]
# # x[2]=4
# x.append(4,5)
# print(x)

# CARA MENGHAPUS ARRAY
# binatang = ['kucing', 'rusa', 'badak', 'gajah']
# del binatang[2]
# print(binatang)

# # CARA SLICING 
# s = "Hello World!"
# print(s[4]) 		#ambil karakter kelima dari string s
# print(s[6:11]) 		#ambil karakter ketujuh hingga sebelas dari string s
# s[5]="d" 		#ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
# s = "Halo Dunia!"	#ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
# print (s)

# # TUPLE : LIST PERMANEN, GABISA DIUBAH. DAN DIDEFINISIKAN PAKAI KURUNG BIASA
# t = (5,'program', 1+3j)
# print(t[1])
# print(t[0:3])
# print(t[0]=10) 

# SET : LIST TANPA ADA URUTAN. DIDEFINISIKAN PAKAI KURUNG KURAWAL
# KARENA SIFATNYA TIDAK BERATURAN,MAKA KITA TIDAK BISA MELAKUKAN SLICING PADA SET
# TIDAK BISA DIPANGGIL DENGAN ANGKA INDEKS.
# a = {1,2,2,3,3,3}
# print(a)
# print(a[1]) #PROGRAM TIDAK JALAN



# DICTIONARY
# Dictionary pada Python adalah kumpulan pasangan kunci-nilai (pair of key-value) 
# yang bersifat tidak berurutan.
# dan tidak bisa dipanggil dengan angka indeks

# d = {1:'value','key':2}
# print(type(d))
# print("d[1] = ", d[1])
# print("d['key'] = ", d['key'])





# CONVERT ANTAR TIPE DATA

# # float to 
# print(int(10.5))
# print(float(13))
# print(tuple({1,2,3}))
