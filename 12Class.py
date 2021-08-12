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

