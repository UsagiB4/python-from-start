import subprocess
subprocess.run(["echo", "Hello world"], shell=True)

ips = subprocess.run(["ipconfig"], capture_output=True, shell=True)  # this will show you the ip. same as `ifconfig` in linuxOS.
print(ips.stdout)  # this will return weird output. all in one line. to remove that simply add `text=True`.
# that will stringify the output.

subprocess.run("cd .. & dir", shell=True)  # running multiple commands in one line. ``commands are for windows only``.
subprocess.run(["cd", "..", "&", "dir"], shell=True, stdout=True)  # this will also execute multiple commands.

with open('sample.txt', 'w') as f:
    fileList = subprocess.run(["dir"], stdout=f, text=True, shell=True)  # redirecting the output text to sample.txt

