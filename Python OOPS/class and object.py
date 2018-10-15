class Peacock:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
ip = Peacock("Indian_Peacock", 10)
gp = Peacock("Green_Peacock", 15)

# access the class attributes
print("obj1 is a {}".format(ip.__class__.species))
print("obj2 is also a {}".format(gp.__class__.species))

# access the instance attributes
print("{} is {} years old".format( ip.name, obj1.age))
print("{} is {} years old".format( gp.name, obj2.age))

'''In the above program, we create a class with name Peacock. Then, we define
attributes. The attributes are a characteristic of an object.

Then, we create instances of the Peacock class. Here, ip and gp are references
(value) to our new objects.

Then, we access the class attribute using __class __.species. Class attributes
are same for all instances of a class. Similarly, we access the instance
attributes using ip.name and gp.age. However, instance attributes are
 different for every instance of a class.'''
