import subprocess
import shlex

myCmd = "cd & dir"
args = shlex.split(myCmd)  # this will split the string and return a list.
print(args)

output = subprocess.Popen(args, shell=True)

print(output)
print("Output.wait() = ", output.wait())  # returns 0 if the process is successful

