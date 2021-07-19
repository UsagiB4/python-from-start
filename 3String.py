"""
String is a big term to discuss.
In python a string is kept in either single quote or double quote.
"""
aString = "This is a string"
bString = 'This is also a string'
# Multiline string can be assigned within 3 single/ double quotation.
multiLin = """ Hello There, 
This is a multiline string.
Python is amazing.
"""

#-_-_-_-_-_-_-| Sting Length |-_-_-_-_-_-_-
# len()
a = len(aString)  # this will show the length of the string
#-_-_-_-_-_-_-| Check string |-_-_-_-_-_-_-
# in & not in
check1 = 'This' in bString  # this will return true if 'This' exists in bString
check2 = 'Now' not in aString  # this will return true if 'Now' does not exist in aString

#-_-_-_-_-_-_-| Slicing |-_-_-_-_-_-_-
# Slicing in string is like List.
# You can easily slice string with index number.
slc1 = multiLin[0: 4]
slc2 = multiLin[-1: -8]
slc3 = multiLin[:6]

#-_-_-_-_-_-_-|Modifying string|-_-_-_-_-_-_-
# _.upper() & _.lower()
word1 = "sciENce"
upperCase = word1.upper()  # This will make all the latter in the variable Uppercase
lowerCase = word1.lower()  # This will make all the latter in the variable Lowercase


# _.replace(a, b) ---- here a will be replaced by b
location = "England"
location = location.replace("E", 'P')

# _.split(split_point)
sentence1 = 'This is so sweet.'
spl1 = sentence1.split('s')

# _.format(var1, var2, var3)
age = 10
name2 = 'Tom'
color1 = 'Green'
print("this is {1}. He is {0} years old.".format(age, name2))  # the variable in the format() function has index number. You can assign them using that index
print("this is {}. He is {} years old. His favourite color is {}".format(name2, age, color1))  # you also can use without indexing. But in that case you must put them in the order you want them to be.

#-_-_-_-_-_-_-|Scape character|-_-_-_-_-_-_-
# you can not use double quote in double quote. that's when scape character comes to help you
print("I love \"Rocket Science\" ")
"""
\n to create new line
\t to open a new tab
\\ to add a \ in the line
"""
