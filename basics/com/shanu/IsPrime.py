x = int(input("Enter a number"))
if x >1:
    for i in range(2,x):
        if x % i == 0:
            print("Entered number is not a prime number")
            break
    else:
         print("Entered number is a prime number")
else:
    print("Entered number is not a prime number")
