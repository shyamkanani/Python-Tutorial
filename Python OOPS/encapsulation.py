'''Using OOP in Python, we can restrict access to methods and variables. This
 prevent data from direct modification which is called encapsulation. In Python,
 we denote private attribute using underscore as prefix i.e single " _ " or
 double " __".'''

class Computer:

    def __init__(self):
        self.__maxprice = 10000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 11000
c.sell()

# using setter function
c.setMaxPrice(11000)
c.sell()

'''In the above program, we defined a class Computer. We use __init__() method
to store the maximum selling price of computer. We tried to modify the price.
However, we can’t change it because Python treats the __maxprice as private
attributes. To change the value, we used a setter function i.e setMaxPrice()
which takes price as parameter.'''
