import os
# Operating system Module.
print(os.getcwd())  # this will show you your current working directory.
print("Type your dir path: ")
dirP = input()  # asking for directory path.
os.chdir(dirP)  # this will change your current working directory to the given path.
print(os.getcwd())
makeDir = input("Do you wanna make a folder? Y/N ")
if makeDir.upper() == 'Y':
    print("Type the name: ")
    folder_name = input()
    os.mkdir(folder_name)
elif makeDir.upper() == 'N':
    print("Exiting without error")
else:
    print("value error")
