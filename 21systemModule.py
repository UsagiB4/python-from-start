# system module and how to use it

import sys

print(sys.argv)  # sys.argv returns a list that contains the program's path.
"""
you can pass argument in the program from terminal. 
e.g- python <pythonFileName.py> arg1, arg2, arg2

this will return a list where the python file will at index 0.
>>> ['path/of/python/file', 'arg1', 'arg2', 'arg3']
"""
# let's write a simple code that adds some numbers

argument_list = sys.argv
del argument_list[0]
result = 0
for i in range(len(argument_list)):
    num1 = argument_list[i]
    num1 = int(num1)
    result = num1 + result
    i += 1
print(result)
