# cara mendefinisikan fungsi

# def nama_fungsi( parameter )
# contoh:
# def nama(name):
#     print(name)
#     return 
# nama("Tiara")


# def luas(p,l):
#     luas=p*l
#     print(luas)
#     return luas
# luas(3,4)


# Pass by reference vs value
def ubah(list_saya):
    list_saya.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(list_saya))

list_saya=[0,1,2]
ubah(list_saya)
print('Nilai di luar fungsi: {}'.format(list_saya))

# PRINT DIDALAM DAN DILUAR FUNGSI AKAN SAMA KARENA FUNGSI DARI .APPEND SENDIRI ADALAH MENAMBAHKAN VALUE PADA LIST,
# JADI, KETIKA KITA MEN-PRINT BAIK DI DALAM ATAU DILUAR FUNGSI HASILNYA AKAN SAMA SAJA.

# CARA KERJA:
# a. untuk nilai di dalam fungsi,
# def ubah(list_saya):
#     list_saya.append([0,1,2])
#     print("nilai dalam fungsi : {}" .format(list_saya))
# ubah([5,4,3])
# list_saya.append([0,1,2])
# list_saya=[5,4,3]
# print("nilai dalam fungsi : {}" .format(list_saya))


# def ubah(list_saya):
#     "Deklarasi Variabel list_saya berikut hanya dikenali (berlaku) di dalam fungsi ubah"
#     list_saya = [1, 2, 3, 4] 
#     print ('Nilai di dalam fungsi: {}'.format(list_saya))
 
# # Panggil fungsi ubah
# list_saya = [10, 20, 30]
# ubah(list_saya)
# print('Nilai di luar fungsi: {}'.format(list_saya))


