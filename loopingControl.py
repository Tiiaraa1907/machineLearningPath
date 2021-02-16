# 1. BREAK : menghentikan perulangan
for i in range (0,10):
    for j in range (0,10):
        if j>i:
            print()
            break
        else:
            print("*",end="")

# CONTINUE : skip
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

# FOR ELSE : ELSE SETELAH FOR
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break

# WHILE ELSE : ELSE SETELAH WHILE
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

# PASS : JIKA INGIN MEMBUAT STATEMENT NAMUN TIDAK MAU MELAKUKAN APA-APA
def sebuahfungsi():
    pass

# LIST COMPREHENSION
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

#Contoh4 Implementasi dengan list comprehension
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat) # Output: ['d','i']

list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a)
