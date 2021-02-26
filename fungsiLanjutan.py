# def printinfo(*args, **kwargs):
#     for a in args:
#         print('argumen posisi {}'.format(a))
#     for key, value in kwargs.items():
#         print('argumen kata kunci {}:{}'.format(key, value))
 
 
# # Panggil printinfo
# printinfo()
# printinfo(1, 2, 3)
# printinfo(i=7, j=8, k=9)
# printinfo(1, 2, j=8, k=9)
# printinfo(*(2, 3), **{'i':7, 'j':8})

# Jadi, tanda * berarti untuk 1 argumen, contoh: 1,2,3 a,b,c (jadi setiap pemanggilan fungsi yang berupa 1 argumen,
# akan diberikan pada args), begitupun pada tanda **, setiap ada pemanggilan "key" dan "value", akan diberikan
# kepada kwargs




# FUNGSI ANONIM (LAMBDA)
kali = lambda nilai1, nilai2,: nilai1 * nilai2
print ("Hasil : ", kali( 11, 21 ))
print ("Hasil : ", kali( 2, 2 ))
