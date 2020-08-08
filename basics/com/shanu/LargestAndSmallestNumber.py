mylist = [5,15,100,4,9]

print ("maximun number is", max(mylist))
print ("minimun number is", min(mylist))

# find the largest value

mylist = [5,15,100,4,9,5000]
largest = mylist[0]
for x in mylist:
    if x > largest:
        largest = x
print ("largest number is", largest)

# find the smallest value
mylist = [5,15,100,4,9,5000]
smallest = mylist[0]
for x in mylist:
    if x < smallest:
        smallest = x
print ("smallest number is", smallest)
