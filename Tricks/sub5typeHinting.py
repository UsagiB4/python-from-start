takeNum1 = input("Enter your number ")
takeNum2 = input("Enter your number ")
takeOp = input("Inter the operation sign you want to run: \n + \n - \n * \n / \n>>> ")
takeNum1 = int(takeNum1)
takeNum2 = int(takeNum2)


def adding(a: int, b: int) -> int:
    addition = a + b
    return addition


def subbing(a: int, b: int) -> int:
    if a < b:
        subtraction = b - a
        return subtraction
    else:
        subtraction = a - b
        return subtraction


def divving(a: int, b: int) -> float:
    division = a / b
    return division


if takeOp == '+':
    print(adding(takeNum1, takeNum2))
elif takeOp == '-':
    print(subbing(takeNum1, takeNum2))
elif takeOp == '/':
    print(divving(takeNum1, takeNum2))

