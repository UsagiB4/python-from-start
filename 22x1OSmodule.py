import os

os.chdir('F:/newPythonFile')  # changing my directory
# os.mkdir('newPythonFile')
with open('myfile.txt', 'w') as myfile:  # creating a demo txt file
    pass
os.rename('myfile.txt', 'myfile.pdf')  # renaming myfile.txt to myfile.pdf

#os.remove('myfile.pdf')  # removing the myfile.pdf file

os.mkdir('demo')  # creating a demo folder
os.rmdir('F:/newPythonFile/demo')  # removing demo folder

