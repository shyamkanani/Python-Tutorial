#program for printing letters in the form of a
#                                            bb....
a = int(input("Enter no of rows :"))
for j in range(a):
    k = a
    while k <= j + a:
        print(format(j) , end = " ")
        k += 1
    print()
