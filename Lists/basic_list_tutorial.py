# Author: LoganJM
# Date:   10/6/18

# Lists are roughly defined as a list of variables. Lists are an "iterable" 
# datatype that are very useful for holding a lot of data and have good uses
# in CSV files, for example.

# To create a list, you use commas and the rectangular brackets, [, and ]
# For example, here's a list of numbers called 'numbers'
numbers = [7, 4, 9, 3, 5, 6, 7]

# lists in python are indexed at zero, so to access a certain element in a list
# you use the syntax of "list_name[element_number]". So as an example, we can 
# access the number 5 by using the following statement:
numbers[4]
# to give a better view on how element numbering looks, here is another list
names = ['Alex', 'Bob', 'Stan', 'Susan']
# here is how  elements for this list are set up:
# 'Alex'  =   0
# 'Bob'   =   1
# 'Stan'  =   2
# 'Susan' =   3

# lists can also be made up of many data-types, making them a very powerful
# tool for holding data. For example, here is a List that holds someone's
# contact information
contact = ['Bob', '111-111-1111', '123 Sesame Street']

# since lists are "iterable" we can use a for loop to run through this contact
# information, and print each line.
for element in contact:
    print(element)
# This results in the following output:
#   Bob
#   111-111-1111
#   123 Sesame Street