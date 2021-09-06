# Inheritance in python allows to define a class that inherits all methods and properties from another class.
# Here We need 2 classes:
# 1:--> parent class / which we will inherit from [Rectangle()]
# 2:--> child class / which will inherit from parent class [Squire()]

#_______Parent Class_______
class Rectangle:
    def __init__(self):
        print("Inside init of Rectangle")

    def area(self, x, y):
        return x * y


#_______ Child Class _______
class Squire(Rectangle):
    pass


r = Rectangle()
sq = Squire()
area = sq.area(2,2)
print(area)
