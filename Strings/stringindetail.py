# A string is created by entering text between two single or double quotation marks.
# e.g. create a string with single and double quotes.
string1='python is fun!'
print(string1)
string2="I am programmer"
print(string2)
# python provides an easy way to avoid manually writing "\n" to escape newlines in a string.
#  'customer: good morning.\n owner : good morning ,sir.welcome to the xyz shop.'
# create string with three sets of quotes and newlines that are created by pressing enter are automatically escaped for you.
string3=""" customer: good morning.
owner : good morning ,sir.welcome to the xyz shop."""
print(string3)

# in python individual characters of a string can be accessed by using the method of indexing.

string4="helloworld"
print(string4[0])   # o/p: s
print(string4[-1])  # o/p: d

# slicing in a string is done by using slicing operator(colon).
# printing 2nd to 9th character 
print(string4[2:9])  

# strings are immutable , hence elements of a string cannot be changed  once it has been assigned.
# updation of entire string is possible.

string4="goodafternoon"
print(string4)

# deletion of entire string is possible with the use of del keyword .
#del string4
print(string4)

# string can be formatted with the use of format() method .
string="{} {} {}".format( 'show ','your','code')
print(string)  #o/p: show your code

# formatting of integer 
number="{0:b}".format(8)
print(number)   #o/p:1000
no="{0:e}".format(786.66)
print(no)       #o/p:7866600e+02

# as with integers and floats,string in python can be added, using a process called concatenation.
print("self" + "respect")  # o/p: selfrespect

# string can also be multiplied by integers
print("amazing" * 3)
# o/p:amazingamazingamazing
 