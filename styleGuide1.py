# #identasi 
# # Statement tingkat 1:
# #     Statement tingkat 2()
# #     Statement tingkat 2 yang kedua()

# # Opsi 1
# # Rata kiri dengan kurung atau pemisah dengan argumen utama
# cara nulisnya,
# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)
 
# # Opsi 2
# # Tambahkan indentasi ekstra - (level indentasi baru) untuk memisahkan parameter/argument dari bagian lainnya
# def long_function_name(
#         var_one, var_two, var_three,
#         var_four):
#     print(var_one)
 
# # Opsi 3
# # Hanging indents dengan penambahan level indentasi saja
# bisa kayak gini juga,
# foo = long_function_name(
#     var_one, var_two,
#     var_three, var_four)

# # Hanging indents *boleh* menggunakan selain 4 spasi
# foo = long_function_name(
#   var_one, var_two,
#   var_three, var_four)





# # KONDISI IF
# # Contoh kondisi visual yang tidak diubah/tanpa indentasi
# if (sebuah kondisi dan
#     kondisi yang lain):
#     lakukanSesuatu()
 
# # Tambahkan komentar
# if (sebuah kondisi dan
#     kondisi yang lain):
#     #Mengingat Keduanya Benar, lakukan hal berikut
#     lakukanSesuatu()
 
# # Tambahkan ekstra indentasi pada baris lanjutan
# if (sebuah kondisi dan
#         kondisi yang lain):
#     lakukanSesuatu()

# # LIST
# my_list = [
#     1, 2, 3,
#     4, 5, 6,
#     ]
 
# result = some_function_that_takes_arguments(
#     'a', 'b', 'c',
#     'd', 'e', 'f',
#     )



# my_list = [
#     1, 2, 3,
#     4, 5, 6,
# ]
 
# result = some_function_that_takes_arguments(
#     'a', 'b', 'c',
#     'd', 'e', 'f',
# )


# with open('/path/to/some/file/you/want/to/read') as file_1, \
#      open('/path/to/some/file/being/written', 'w') as file_2:
#     file_2.write(file_1.read())
