# Python open a file using open() function.
# but you have to store the data in a variable to print what's inside the file.
# __open('file name with extension', 'mode') || mode: 'r' = read (default mode) // 'w' = write
a = open('sample.txt', 'r')

#___content = a.read()___  # reading the values
#___print(content)___

content5 = a.read(5)  # this will read the first 5 char from the file.
line = a.readline()  # this will read a line from the file.
lineList = a.readlines()  # this will return a list of lines in the file.
print(content5)
print(line)
print(lineList)

a.close()  # you should close after opening a file


