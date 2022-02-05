import subprocess
import shlex

# ::::::::::Popen.communicate()::::::::::

commandInput = input("Enter your command: ")
args = shlex.split(commandInput)  # here we are splitting the command
print(args)
output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  # executing the command using Popen(). shell=True [ to avoid issues ]
try:
    outP = output.communicate(timeout=5)  # program will terminate after 5 seconds.
    print(outP)
except TimeoutError:
    output.kill()  # terminate the program
    outs = output.communicate()
