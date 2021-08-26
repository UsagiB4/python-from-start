# We use function to prevent repetition of codes
# we can create a function using " def function(parameter): "
def iseven(number):
    num = int(number)
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is not even")


iseven(41)

# Notice that I have used print instead of return.
# if you use Return then you have to put the function in "print()" to print the result.


def isbiggest(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return f"{number1} is the biggest number"
    elif number2 > number1 and number2 > number3:
        return f"{number2} is the biggest number"
    else:
        return f'{number3} is the biggest number'


print(isbiggest(12, 56, 2))

# as the function is just returning the result, so you have to put it in print() function to see it.


