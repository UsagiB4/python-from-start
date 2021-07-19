names = ['Jhon', 'Marry', 'Bob', 'Kate']
#print(names)
"""
Here names is a list which contains some strings.
You can access them with index values
e.g:
"""
#print(names[2])  # This will print 'bob'
#print(names[-1])  # this will print the last value of this list
"""
you also can store floats an integers as values of a list
"""
number_list = [12, 55, 2, 75, 20, 85]
float_list = [3.14, 9.8, 3.33, 5.32, 11.2]

#-_-_-_-_-_-_-_-_-_-|Adding Items|-_-_-_-_-_-_-_-_-_-_-_-
# You can add items in a list in various way.
#_.append(item)
#--------/adds item at the end of the list/--------------
number_list.append(100)

#_.insert(index, item)
#--------/ adds the item in the given index /------------
float_list.insert(2, 99.99)

#_.extend([item/items])
#----------/ adds multiple items to a list /-------------
names.extend(['apple', 'bee', 'rose', 'coffee'])

#-_-_-_-_-_-_-_-|Removing Items|-_-_-_-_-_-_-_-
# there are also various ways to remove item from list
#_.pop() $ _.pop(index)
names.pop()  # this will remove the last item
float_list.pop(3)  # this will remove the item from index no. 3

#_.remove(item)
number_list.remove(55)  # this will remove the item (in this case the item is 55)

# < del aList[index] > & < del alist >
del number_list[3]  # this also deletes item from the given index
del number_list  # this deletes the entire list. If you try to work with that list, it will give you an error

# _.clear()
names.clear()  # this clears the whole list and returns an empty list

#-_-_-_-_-_-_-_-|Shorting a list|-_-_-_-_-_-_-_-
# _.sort() & _.sort(reverse = True)
num_list = [12, 78, 22, 36, 90, 5, 11, 45, 79, 27]
fruits = ['Pineapple', 'Strawberry', 'Apple', 'Guava', 'Dragonfruit', 'Banana', 'Fig', 'Cherry', 'Coconut', 'Nut', 'Grapes']
num_list.sort()
fruits.sort()
# print(fruits)
fruits.sort(reverse=True)
# print(fruits)
# uncomment the print functions to see the result
