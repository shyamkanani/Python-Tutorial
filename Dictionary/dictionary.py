# Author: Luís Duarte, LoganJM
# Date: 07/10/2018

"""
Dictionaries are unordered, dynamic, and mutable (you can change them).

They are different than lists because:
    - Lists are accessed by their position (like 0, 1, 2, 3), but dictionaries
      are accessed by a key of any value
"""

# We can define a dictionary by a pair of curly brackets

dictionary = {}

# To add a value to a dictionary we need a key and a value seperated by a colon

dictionary = {
    'key': "value"
}

# If we want to access we can retrive the value from the dictionary using a
# pair of square brackets [] and the key

print(dictionary['key'])  # It will output 'value'

# To add more than one key to a dictionary we need seperate them by a comma (,)
dictionary = {
    'car': "Ford",
    'year': 2018
}

# If we need to change a value in a key we can:

dictionary['car'] = "BMW"
print(dictionary['car'])  # Instead outputting 'Ford' it will output 'BMW'

# Because dictionaries are dynamic, we can add more values without needing to
# create a new dictionary

dictionary['Model'] = "i3"
print(dictionary)
# It will output {'car': 'Ford', 'year': 2018, 'Model':'i3'} It printed the new
# key and value  that we defined


# To remove a single value:
del dictionary['car']
print(dictionary)  # This will output {'year': 2018, 'Model':'i3'}

# To Remove the WHOLE dictionary is simple:
del dictionary
print(dictionary)  # This will output ValueError: 'dictionary' is not defined.
