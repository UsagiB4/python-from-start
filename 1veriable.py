"""
This is about variable in python
variable is like a container.
You can create a variable with valid name and can store data in it.
The data you store in it defines the type of that variable.
e.g:
>> if you put string in a variable, it will be a string type variable.
>> if you put integer in a variable, it will be a integer type variable.
"""
name = "philosophy"
number = 12
point = 3.14159

#___________Variable Type______________________
print(type(name))  # this will print the type of variable "name"
print(type(number))  # this will print the type of variable "number"
print(type(point))  # this will print the type of variable "Point"
print("_______________________________")  # this is just a line to separate the outputs
#_____________Variable Slicing_____________________
slice_name = name[1:5]
print(slice_name)  # This will print from characters from index 1 to index 4
nth_char = name[5]
print(nth_char)  # This will print the character in index 4
neg_index = name[-1]
print(neg_index)  # This will print the first character from the end
#_______________Multiple Value in Variable______________
x, y, z = 12, 4, 5  # here we are assigning multiple value in multiple variable in a single line
names = ['tim', 'bob', 'Jack']
s, t, r = names  # this will assign the items in list as value of the variables.

