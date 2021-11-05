def fibo(n):
    series = []
    a, b = 0, 1
    while b < n:
        series.append(b)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    usrInput = input("Enter your number: \n")
    usrInput = int(usrInput)
    print(fibo(usrInput))
