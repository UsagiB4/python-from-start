# Dictionary is used to store data in Key:Value format
# Dictionary is ordered and changeable, does not support duplicate value.
a_dic = {
    'name': 'Anna',
    'Age': 23,
    'Location': 'UK',
    'Height': 5.3,
    'Girl': True
}
print(a_dic)

# -_-_-_-_-_-_-_-| Accessing Items in Dictionary |-_-_-_-_-_-_-_-
# values in dictionary can be accessed via Key
print(a_dic['name'])  # this will print the value of 'name' key.
# _.get(key)
age = a_dic.get('Age')  # This does the same

# _.keys()
# this will return a list of keys inside a dictionary
key_list = a_dic.keys()

# _.values()
# same as keys() but returns list of values.
values = a_dic.values()

# _.items()
# returns a list of the items in a dictionary
# where List contains individual tuples for individual items
# in that tuple the first item is key and second item is value
a_car = {
    "car": 'BMW',
    "price": 12000,
    'Currency': 'USD',
    'HP': 360,
    'Color': 'Red'
}
itemList = a_car.items()
itemList = list(itemList)  # by default items() returns 'dict_items' class object
# you have to convert it into a list

# -_-_-_-_-_-_-_-| Updating Dictionary |-_-_-_-_-_-_-_-

# _.update({key : value})
# this will update an existing key:value or add a new key:value
Amy = {
    'age': 24,
    'Home': 'USA',
    'Salary': 1000,
    'Year': 1990,
    'Kids': 2
}
Amy.update({'age': 30})  # This will update the value of key 'age'

# Adding Items
Amy['weight'] = 65  # this will add a new item with key: 'weight' and value: 65

# Removing Items

# _.pop(key)
# this will remove a specified key from the Dictionary
Amy.pop('Kids')

# _.popitme()
# Removes item from dictionary Randomly
Amy.popitem()

# del
# del function has two uses
# 1> it can delete an specific item
# 2> it can delete the entire Dictionary
del Amy['Year']  # this will delete the item with key called 'year'

del Amy  # this will delete the whole Dictionary

# _.clear()
# this clears the whole dictionary and returns an empty dictionary
number = {
    'pi': 3.14,
    'g': 9.8,
    'escape_velocity': 11.2
}
number.clear()

# -_-_-_-_-_-_-_-| Copying Dictionary |-_-_-_-_-_-_-_-


words = {
    'a': 'about',
    'b': 'blank',
    'c': 'cow',
    'd': 'draw',
    'e': 'egg',
    'f': 'flower'
}

# _.copy()
copy_words = words.copy()

# dict()
copy_words2 = dict(words)

# -_-_-_-_-_-_-_-| Nested Dictionary |-_-_-_-_-_-_-_-
# you can put multiple dictionaries into a single dictionary. this is known as nesting
# The dictionaries inside the dictionary is called Nested Dictionaries

boys = {
    'boy1': {
        'name': 'Abe',
        'age': 10
    },
    'boy2': {
        'name': 'Ahmed',
        'age': 12
    },
    'boy3': {
        'name': 'Elon',
        'age': 9
    }
}

# or you can create multiple single dictionaries and put them into a mother dictionary
boy1 = {
    'name': 'Josh',
    'age': 12
}
#___________________________
boy2 = {
    'name': 'Tom',
    'age': 15
}
#___________________________
boy3 = {
    'name': 'Karl',
    'age': 16
}
#___________________________
all_boys = {
    'Boy1': boy1,
    'Boy2': boy2,
    'Boy3': boy3
}
