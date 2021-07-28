# While loop.
# a while loop can execute a bunch of statements if the given condition is true.

#_______ Practice 1 _______
#_____ Multiplication table ______
"""userInput = input("Enter a number: ")
userInput = int(userInput)
counter = 1
while counter <= 10:
    multiplication = userInput * counter
    print(f"{userInput} X {counter} = {multiplication}")
    counter += 1
"""
#_________ Practice 2 _________
#_________ Break _________
#_______ Thermometer Has Broken _________
numInput = input("Enter Temperature: ")
numInput = int(numInput)
limitTemperature = 100
while True:
    if 25 <= numInput <= 28:
        print('Good Temperature.')
        break
    elif 29 < numInput <= 37:
        print('Summer is here')
        break
    elif 57 >= numInput:
        print('You are in desert')
        break
    elif numInput >= 100:
        print('Thermometer is broken')
        break


