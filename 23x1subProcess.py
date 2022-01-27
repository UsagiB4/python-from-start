import subprocess
import shlex

myCmd = "cd & dir"
args = shlex.split(myCmd)
print(args)

output = subprocess.Popen(args, shell=True)

print(output)
print(output.wait())  # returns 0 if the process is successful

