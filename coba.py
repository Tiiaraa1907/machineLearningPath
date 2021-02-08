print("The average of n numbers")
i=1
total=0
count=int(input("The number of integer :"))
while i<=count:
    score= int(input("Input number {} :".format(i)))
    total+=score
    i+=1

avg=total/count
print(avg)
print("The avg of {} numbers is {:.2f}" .format(count,avg))
    