# PERULANGAN FOR
for huruf in 'Dicoding':  # Contoh pertama
    print('Huruf: {}'.format(huruf))
 
flowers = ['mawar', 'melati', 'anggrek']
for flower in flowers:  # Contoh kedua
    print('Flower: {}'.format(flower))

for index in range(len(flowers)):
    print('Flowers: {}'.format(flowers[index]))


# PERULANGAN WHILE
count = 0
while (count < 7):
    print('Hitungannya adalah: {}'.format(count))
    count +=1


# PERULANGAN BERTINGKAT
for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()