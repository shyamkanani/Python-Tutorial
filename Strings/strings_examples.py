# This program shows working of different functions of the strings
str1 = "this is the 1st string"
str2 = "this is the 2nd string"

print(str1.capitalize())
#This is the 1st string

print(str2 , str1.center(50))
#this is the 2nd string               this is the 1st string

str3 = "HELLO WORLD"
print(str3.casefold())
#hello world

print("Number of times 'is' is used in str2 :" ,str2.count('is'))
#Number of times 'is' is used in str2 : 2

print("Is str2 ending with 'f' ?" ,str2.endswith('f'))
#Is str2 ending with 'f' ? False

print(str1.encode())
#b'this is the 1st string'

print("1st occurrence of 's' in str2 : " ,str2.find('s'))
#1st occurrence of 's' in str2 :  3

print("Is str1 in lower case ?" ,str1.islower())
#Is str1 in lower case ? True

print("Is str3 in upper case ?" ,str3.isupper())
#Is str3 in upper case ? True

print("*".join(str1))
#t*h*i*s* *i*s* *t*h*e* *1*s*t* *s*t*r*i*n*g

print(str2.ljust(13))
#this is the 2nd string

print(str1.swapcase())
#THIS IS THE 1ST STRING

print(str2.partition('2'))
#('this is the ', '2', 'nd string')

print(str2.maketrans(str1, str2))
#{116: 116, 104: 104, 105: 105, 115: 115, 32: 32, 101: 101, 49: 50, 114: 114, 110: 110, 103: 103}

print(str1.replace('is' , 'are'))
#thare are the 1st string

print(str2.title())
#This Is The 2Nd String

print(bool(str1))
#True

#print(compile(str1,'strings_examples', 'exec'))
#


print(complex(1,4))
#(1+4j)

str4 = '345'
print(int(str4))
#345

print("length of str2 :" ,len(str2))
#length of str2 : 22

print("maximum of str2 :" ,max(str2))
#maximum of str2 : t

print("minimum of 'hello' :" ,min('hello'))
#minimum of 'hello' : e

print(map(str2, str1))
#<map object at 0x000001C492128198>

print(reversed(str3))
#<reversed object at 0x000001D4EDAC81D0>

print(slice(str3[1:10]))
#slice(None, 'ELLO WORL', None)

print(sorted(str3))
#[' ', 'D', 'E', 'H', 'L', 'L', 'L', 'O', 'O', 'R', 'W']


print(zip(str3))
#<zip object at 0x000001BA6A32BD88>
