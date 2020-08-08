x = int(input("Enter a number to find factorial"))
factorial = 1
if x < 0:
    print("There is no factorial for negative numbers")
elif x == 0:
    print("Factorial of zero is 1")
else:
    for i in range(1,x + 1):
        factorial = factorial*i
    print("Factorial of a number", x, "is", factorial)