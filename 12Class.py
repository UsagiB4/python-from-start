# Class in python can be create using the word 'class'.
class MyName:
    userName = 'Jhon'


# Creating an object
objA = MyName()
print(objA.userName)


# __init__ function
# __init__ function assigns value(s) which are needed when the object is created
class NewObject:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        addition = self.number1 + self.number2
        return addition


newObj = NewObject(23, 2)
print(newObj.add())

# we also can modify the property of an object
# now number2 will have the value 10 instead of 2
newObj.number2 = 10
print(newObj.add())

# Deleting Object Property
del newObj.number2
# the code will remove/ delete property number2 from object newObj
# if you try to print the object with that property, it will through "AttributeError"


# Deleting Object
del newObj


# this will delete the newObj.


# _______ Pass ___________
# Class can not be empty. So You have to put something in it
# If you have nothing to put in a class, you can use "Pass Statement" to avoid getting error.

class RandomClass:
    pass

    # _________Static Method_______
    @staticmethod
    def say_hi():
        print('Hello There, This is static method')
    # static method does not have "self" in it. SO it does not need any value to run. It can be run just by calling it.


objectA = RandomClass()
objectA.say_hi()
