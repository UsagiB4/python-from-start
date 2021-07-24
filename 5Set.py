# Set in python is a collection of both unordered and unindexed values.
a_set = {12, 3, 4, 1, 67, 33, 24}

# if you print a set, it will change the index of its values.

#-_-_-_-_-_-_-_-| Accessing the Values |-_-_-_-_-_-_-_-
# you can not access the values in a set with index/ key

#-_-_-_-_-_-_-_-| Adding Items |-_-_-_-_-_-_-_-
# _.add(item)
this_Set = {'World', 'round', 24, True, 'Clock', 654, False}
this_Set.add('New')  # this will add a new item to the set in a random place.

# _.update(anotherSet)
# this method will help you to add a set with other
set1 = {'hello', 'Ohio', 'Good'}
set2 = {1, 3, 5}
set1.update(set2)
# You can also add list to a set using update() methode
# Result will be a single set

#-_-_-_-_-_-_-_-| Removing Item from a set |-_-_-_-_-_-_-_-
# _.remove(item) & _.discard(item)
set1.remove('hello')  # this will remove the item 'hello'.
set1.discard('Good')  # this will remove the item 'Good'.
# The difference between remove() and discard() is, if the removing item doesn't exist in set
# remove() will give you an error but discard() will not give you any error.

# _.pop()
setA = {'banana', 'boat', 'bird', 'bowl'}
setA.pop()
"""
this will remove the last item from the set. 
But items in set are unindexed, so you will not know which one is the last item.
"""
# _.clear() & del
setA.clear()  # this will remove all the items from the set.
del setA  # this will delete the set completely.


#-_-_-_-_-_-_-_-| Joining sets |-_-_-_-_-_-_-_-
# _.union(anotherSet)
numbersA = {1, 2, 4, 7, 12, 9}
numbersB = {1, 3, 4, 5, 10, 12}
numberC = numbersB.union(numbersA)  # This will marge the sets into a new set
#______there are some other join methods like:
"""
intersection_update() >method will keep only the items that are present in both sets.
intersection() >method will return a new set, that only contains the items that are present in both sets.
symmetric_difference_update() >method will keep only the elements that are NOT present in both sets.
symmetric_difference() >returns a new set, that contains only the elements that are NOT present in both sets.

"""

