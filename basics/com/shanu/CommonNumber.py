list1 = [1,2,3,4,5]
list2 = [2,4,7,1,5]
print(set(list1) & set(list2))

list1 = [1,2,3,4,5]
list2 = [2,4,7,1,5]
commonlist = []
for i in list1:
    for j in list2:
        if (i == j):
            if(not(i in commonlist)):
                commonlist.append(i)
print ("Common numbers are", commonlist)
