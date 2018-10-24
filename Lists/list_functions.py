# Author : Rayudubobbili

# List functions

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# append
l.append(0)  # append '0' at the end of the list. [1,2,3,4,5,6,7,8,9,0]

# pop
l.pop()  # remove last item from the list. [1,2,3,4,5,6,7,8,9]

# insert
l.insert(0, 0)  # insert '0' at the 0 index. [0,1,2,3,4,5,6,7,8,9]

# remove
l.remove(9)  # remove '9' from the list. [0,1,2,3,4,5,6,7,8]

# reverse
l.reverse()  # reverse the indexes of the list. [8,7,6,5,4,3,2,1]

# index
l.index(8)  # return the index of item '8' that is 0

# count
l.count(1)  # return how many '1' items available in list

# sort
s = ['a', 'A', 'b', 'B']
l.sort()  # sort the entire list.
s.sort()  # ['A', 'B', 'a', 'b']. Sort put captial letters first

# copy
s = l.copy()  # Copy entire list to 's' variable

# clear
s.clear()  # clear all items from 's' variable

# extend
s = ['a', 'b']
s.extend(l)  # extends the 's' list with 'l' items. ['a','b',8,7,6,5,4,3,2,1]

# length
len(l)  # return the lenght of items in a list. 8
