import fibon

usrInput = input("enter the number: \n")
usrInput = int(usrInput)
fiboS = fibon.fibo(usrInput)
print(fiboS)
for items in fiboS:
    print(items)
