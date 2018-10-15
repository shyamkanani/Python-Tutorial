'''Methods are functions defined inside the body of a class. They are used to
define the behaviors of an object.'''

print(blu.dance())class Peacock:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
ip = Peacock("Indian_Peacock", 10)

# call our instance methods
print(ip.sing("'Happy'"))

'''In the above program, we define two methods i.e sing() and dance().
These are called instance method because they are called on an instance object
i.e ip.

 '''
