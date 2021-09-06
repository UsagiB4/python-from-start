# An Iterator is an object that contains countable number of values.
# List, Tuple, Set, Dictionary, Strings are considered as iterators. You can iterate trough them.

# ______ simple iteration ______
myList = ['apple', 'orange', 'banana', 'egg', 'star', 'key']
myiter = iter(myList)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(myiter.__next__())  # you can also use .__next__() to print the next value.
print(myiter.__next__() + "\n")

color_list = ['red', 'yellow', 'green', 'blue', 'cyan', 'pink', 'white']
iter_color = iter(color_list)
for i in range(len(color_list)):
    print(iter_color.__next__())
