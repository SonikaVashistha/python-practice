def pyramid(p):
    X = 2*p - 2 # 14
for m in range(0, p): # m = 0 to 10, 1
    for n in range(0, X): # n= 0 to 16
        print(end=" ")
    X = X - 2
    for n in range(0, m+1): # n = 0 to 2
        print("* ", end="")
    print("\r")
p = 10
pyramid(p)


# ------------------*
# ----------------* *
#
