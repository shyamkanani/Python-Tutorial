''' Polymorphism is an ability (in OOP) to use common interface for multiple
form (data types).

Suppose, we need to color a shape, there are multiple shape option (rectangle,
square, circle). However we could use same method to color any shape. This
concept is called Polymorphism.'''

class Rose:

    def color(self):
        print("Red")

    def characteristic(self):
        print("Represents love.")

class Lavendar:

    def color(self):
        print("Purple")

    def characteristic(self):
        print("Represents refinement, grace, and elegance.")

# common interface
def test(flower):
    flower.color()
    flower.characteristic()

#instantiate objects
ros = Rose()
lav = Lavendar()

# passing the object
test(ros)
test(lav)
