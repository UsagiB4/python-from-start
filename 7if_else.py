# Vampire Tester
# De-comment to run the code
"""user_input = int(input('Enter your age: '))
user_input = abs(user_input)
if user_input < 18:
    print('You are a human kid')
elif 18 <= user_input <= 40:
    print('You are an adult')
elif 41 <= user_input <= 60:
    print('You are old')
elif user_input <= 100:
    print('Good to see you old man')
else:
    print('You are a vampire. Have fun learning Python')"""


# big number
num1, num2, num3 = input("Enter 3 numbers").split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1 > num2 and num1 > num3:
    print(f"{num1} is the biggest number")
elif num1 < num2 and num2 > num3:
    print(f"{num2} is the biggest number")
else:
    print(f"{num3} is the biggest number")

