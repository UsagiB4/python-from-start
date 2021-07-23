#Tuple is one of the 4 data types in python.
#you can create a tuple by using () round brackets
aTuple = ("Hello", "World", "Moon", "Sea", "Earth", "Tree", "Food", "Bird", "Sun")
singleTuple = ("Single",)  # You can create a single value tuple like this.
print(aTuple)

# Tuple is immutable. That means you can not change the value of a tuple once you have created it.
# aTuple.append/ .remove/.extend are not allowed and will give you an error.
tuple_Type = (type(aTuple))
tuple_length = (len(aTuple))

#_-_-_-_-_-_-_-| Accessing Items in A Tuple |_-_-_-_-_-_-_-
#just like list, items in tuple can be accessed with index number
print(aTuple[1])  # will give you the second item in the tuple.
print(aTuple[2:5])  # this will print the the items from index 2 to index 4.

# checking if the item is in the tuple
print("Tree" in aTuple)  # will return "True"


#_-_-_-_-_-_-_-| Updating Tuple |_-_-_-_-_-_-_-
"""
    Tuple is immutable, which means after you create a tuple you can not upgrade it.
    But there is some ways to update (more like make a copy of an existing tuple) a tuple.
"""
# _________ Method 1___________
old_tuple = ('water', 'cat', 24, 'nine', True, 7)
copy_List = list(old_tuple)  # this will turn the tuple into a list named "copy_List"
copy_List.append('NewThing')  # this will add 'NewThing' to the list.
new_tuple = tuple(copy_List)  # this will turn the list into a tuple.

# And like that you can update a tuple.

#_______ Method 2 __________
# tuple allows add one tuple with another. This can also be used to update a tuple
tuple_A = (24, 7, 365, 12)
tuple_B = ('Day', 'night', 'Year')
tuple_A += tuple_B
print(tuple_A)


#_-_-_-_-_-_-_-| Deleting Item from Tuple |_-_-_-_-_-_-_-
# There is no such thing as "Deleting" in tuple as it is unchangeable.
# But you can delete the entire tuple.
del tuple_A
# Print(tupel_A) now will give you an error as tuple_A no longer exists.



