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

# Writing a file. if you open a file in 'w' mode,
# you will be able to write into the file.
# But remember, this will delete all the previous content in the file and add the new content(s)
filew = open('sample.txt', 'w')
filew.write('a new line')
filew.close()

# Appending in a file using python
# 'w' mode removes the previous contents from the file. To stop that you have to use append mode 'a'.
# this will add new content keeping the previous contents.


fileA = open('sample.txt', 'a')
fileA.write('Appending a new line\n')
fileA.write('another new line')
fileA.close()

# Creating a new file using python
# open('generate.txt', 'x')  # this will create a new text file called generate.txt

gen = open('generate.txt', 'a')
gen.write('adding new line\n')
gen.close()
