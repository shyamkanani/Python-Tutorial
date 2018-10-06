"""A tuple is a sequence of immutable objects, therefore tuple cannot be changed. It can be used to collect different types of object.

The objects are enclosed within parenthesis and separated by comma.

Tuple is similar to list. Only the difference is that list is enclosed between square bracket, tuple between parenthesis and List has mutable objects whereas Tuple has immutable objects.

"""
tp = (1,"SK",28)
tp1 = 3,"DK",10 

print(tp) # output : (1,"SK",28)
print(tp1) # output : (3,"SK",10)

tp2 = tp1,(20,"RK")
print(tp2) # output : ((3,"SK",10),(20,"RK"))

#Tuple Acessing Mechanisms

print(tp[0]) # 1
print(tp[1:3]) # ("SK",28)
print(tp[-1]) # 28

tp[0] = 2 # Raise an TypeError: 'tuple' object does not support item assignment

#Tuple Operations 

tp3 = tp + tp1 
print(tp3) # (1,"SK",28,3,"DK",10)

del tp2 # Will delete the entire tuple
min(tp) # 1
max(tp1) # 10
len(tp3) # 6

#if len(tp) > len(tp1) then output is 1
#if len(tp) = len(tp1) then output is 0
#if len(tp) < len(tp1) then output is -1

print(cmp(tp,tp3)) # -1




