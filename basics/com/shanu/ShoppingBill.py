print ("**Welcome to the Grocery Shop**")
items = ("apple","bread","milk","banana","butter")
price = (100,30,25,50,80)
qty = (0,0,0,0,0)
i = 0
for x in items:
    qty[i] = int(input("Enter the %s quantity " % x))
    i = i+1
i = 0
for x in items:
    if(not(qty==0)):
        print("%s %d kg = Rs. %.2f" %(x, qty(i), qty(i)*price(i)))
        i = i+1