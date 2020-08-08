mylist = []
mylist.append(10)
mylist.append(25)
mylist.append(100)
mylist.append(17)
mylist.append(19)
for i in mylist:
    remainder = i % 5
    if remainder ==0:
        print (i)