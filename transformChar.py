# upper
# kata = 'dicoding'
# kata = kata.upper()
# print(kata)

# lower
# kata = 'DICODING'
# kata = kata.lower()
# print(kata)

# # rstrip (hapus spasi belakang)
# print('Dicoding    '.rstrip())

# # lstrip (hapus spasi depan)\
# print('    Dicoding'.lstrip())

# # strip (hapus spasi depan belakang, dan menghapus kata)
# print('    Dicoding    '.strip())
# kata = 'CodeCodeDicodingCodeCode'
# print(kata.strip('Code'))

# # startswith(boolean)
# print('Dicoding Indonesia'.startswith('Dicoding'))

# # ends  with()
# print('Dicoding Indonesia'.endswith('Indonesia'))


# # MENGGABUNGKAN STRING
# print(' '.join(['Dicoding', 'Indonesia', '!']))
# print('123'.join(['Dicoding', 'Indonesia', '!']))

# # MEMISAHKAN STRING
# print('Dicoding Indonesia !'.split())
# # BISA DIGUNAKAN PADA MULTILINE
# print('''Halo,
# aku ikan,
# aku suka sekali menyelam
# aku tinggal di perairan.
# Badanku licin dan renangku cepat.
# Senang berkenalan denganmu.'''.split('\n'))

# # MENGGANTI STRING
# string = "Ayo belajar Coding di Dicoding"
# print(string.replace("Coding", "Pemrograman"))
# # JIKA ADA 2 KATA YANG SAMA
# string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
# print(string.replace("Coding", "Pemrograman", 1))

# ISUPPER (isupper() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf besar,
#  dan akan mengembalikan nilai False jika terdapat satu saja huruf kecil di dalam string tersebut.)
# kata = 'DICODING'
# kata.isupper() #HASILNYA TRUE

# kata = 'dicoding'
# kata.isupper() #HASILNYA FALSE

# # ISLOWER (kebalikan dari metode isupper())
# kata = 'DICODING'
# kata.islower() #HASILNYA FALSE

# kata = 'dicoding'
# kata.islower() #HASILNYA TRUE

# # ISALPHA (semuanya alphabet) 
# 'dicoding'.isalpha()
# # ISALNUM(ada semua/salah satu alphabet number)
# 'dicoding123'.isalnum()
# # ISDECIMAL (semuanya angka)
# ‘12345’.isdecimal()
# # ISSPACE(spasi)
# ' ' .isspace()
# # ISTITLE (jika huruf besar setiap kata)
# 'Dicoding Idn' .istitle()

# # ZFILL (zero fill,, jika kita type zfill(5), maka ada 0 sebanyak 4 kali)
# # Contoh 1: Penggunaan zfill 5 pada angka satuan
# angka = 5
# print (str(angka).zfill(5))
# # Contoh 2: Penggunaan zfill 5 pada angka ratusan
# angka = 300
# print (str(angka).zfill(5))
# # Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
# angka = -0.45
# print (str(angka).zfill(5))
# # Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
# angka = -0.45
# print (str(angka).zfill(7))

# # Contoh 1
# kata = 'aku'
# print (kata.zfill(5))
# # Contoh 2
# kata = 'kamu'
# print (kata.zfill(5))
# # Contoh 3
# kata = 'dirinya'
# print (kata.zfill(5))

# rjust(rata kanan)
'Dicoding'.rjust(20)
# ljust(rata kiri)
'Dicoding'.ljust(20)
# center
'Dicoding'.center(20,'-')

# STRING LITERAL
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash

# berikut adalah multiline
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""
print(multi_line)


# RAW STRING (sesuai syntax)
print(r'Dicoding\tIndonesia')