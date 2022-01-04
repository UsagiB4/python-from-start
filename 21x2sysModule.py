import sys

#_____sys.stdin_______
# sometimes user might need to keep the input into a custom log. That's when 'stdin' comes to help.
print("Enter your name and age: \n")
usr_name = sys.stdin.readline()
age_num = sys.stdin.readline()
sys.stdout.write(f"Your name is {usr_name}")

