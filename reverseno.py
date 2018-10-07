n=int(input("Enter number:"))
rev = 0
while(n>0):
    red = n%10
    rev = (rev*10) + red
    n=n//10
print("Reverse of number:%d" %rev)
