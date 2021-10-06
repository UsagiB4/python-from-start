insertNumber = input("Please insert a number")

try:
    insertNumber = int(insertNumber)
    add = 20 + insertNumber
    print(f"20 + {insertNumber} = {add}")
except Exception as ex:
    print(ex)

