#  @classmethod
class simpleMath:
    def __init__(self):
        pass

    def add(self, x, y):
        c = x + y
        return c

    def sq(self, x):
        return x ** 2

    @classmethod
    def pow(self, x, y):
        return x ** y


if __name__ == "__main__":
    thisMath = simpleMath()
    print(thisMath.add(12, 3))
    print(thisMath.sq(4))
    #______________Classmethod example_____________
    print(thisMath.pow(3, 3))
    print(simpleMath.pow(4, 2))
    #  print(simpleMath.sq(3))
    """
    @Classmethod decorator helps you to call
    a function inside a class without creating an object.
    In the example you can see that we can use both 'thismath.pow()' and 'simpleMath.pow()'
    as the function _.pow() is in a @classmethod decorator.  
    If you try to use other functions without object, it will through a 'TypeError'
    decomment the code to see the difference.
    """
    # there are other decors too.
    # like
    # @staticmethod which works same as @classmethod.
    # the only difference is @staticmethod doesn't let you use 'self' while creating the function
    # in short, you have make it as a normal function
