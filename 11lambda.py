# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.

# lambda arg : exp

x = lambda y, z: y ** z  # this is a single line lambda that's powers Y by Z
print(x(5, 2))

number = lambda y: y ** (1/2)
print(number(9))
