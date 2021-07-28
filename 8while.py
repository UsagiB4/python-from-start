# While loop.
# a while loop can execute a bunch of statements if the given condition is true.

#_______ Practice 1 _______
#_____ Multiplication table ______
userInput = input("Enter a number: ")
userInput = int(userInput)
counter = 1
while counter <= 10:
    multiplication = userInput * counter
    print(f"{userInput} X {counter} = {multiplication}")
    counter += 1




