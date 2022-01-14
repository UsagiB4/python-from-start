#___________os.path_____________
# `path` is a sub_module of os module.

import os

# .basename() >> returns only the file name.
baseName = os.path.basename('D:\Projects\pythonRev\/7if_else.py')
#print(baseName)

# .dirname() >> returns the directory path of a file.
dir_path = os.path.dirname('D:\Projects\pythonRev\/7if_else.py')
#print(dir_path)

# .exists() >> checks if the file exist in the directory. Returns True if exists, returns False if not.
find_file = os.path.exists('D:\Projects\pythonRev\/7if_else.py')
print(find_file)

# .isdir() >> checks if the directory exists or not. same as .exists() function.
find_dir = os.path.isdir('D:\Projects\pythonRev')
print(find_dir)

# .isfile() >> checks if the given file exists or not. same as .exists() function
find_file = os.path.isfile('D:\Projects\pythonRev\/22x2OSmodule.py')
print(find_file)

# .join() >> joins file name to path. very handy function while making some tools.
dir_name = os.getcwd()  # getting current working dir name.
print(dir_name)
join_path = os.path.join(dir_name, '22OSmodule.py')  # joining the file name with the path
print(os.path.isfile(join_path))  # checking if the file exists or not.

# .split()  >> another useful function. exact opposite of .join() function.
# this function separates directory path from file name and returns a `tuple`
print(os.path.split(join_path))

# .system('command') >> this will help you to run CLI commands in your python program.
# I tested this code on windows machine where 'ipconfig' shows the ip address.
# If you run linux, use 'ifconfig' to get the same result.
print(os.system('ipconfig'))



