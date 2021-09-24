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
