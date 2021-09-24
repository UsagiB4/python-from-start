class MyClass:
    def __init__(self, var):
        self.var = var

    def sqr(self):
        squire = self.var ** 2
        return squire

    def __del__(self):
        print('class has been deleted')

    def add_one(self):
        add = self.var + 1
        return add


self_obj = MyClass(2)
print(self_obj.sqr())
del self_obj  # this will delete the object
#  print(self_obj.add_one())


#____________ Comparison Magic Methods ____________
num1 = 23
num2 = 4

print(num1.__eq__(num2))  # checks if 2 variables are equal
print(num1.__ne__(num2))  # same as not equal or !=
print(num2.__lt__(num1))  # less than
print(num1.__gt__(num2))  # greater than
print(num1.__le__(num2))  # less than or equal
print(num1.__ge__(num2))  # greater than or equal
