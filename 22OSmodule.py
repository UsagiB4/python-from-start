import os
# Operating system Module.
print(os.getcwd())  # this will show you your current working directory.
print("Type your dir path: ")
dirP = input()
os.chdir(dirP)  # this will change your current working directory to the given path.
print(os.getcwd())
