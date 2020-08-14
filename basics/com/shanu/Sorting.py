#ascending
list1 = [1,5,6,9,7,3]
list1.sort()
print (list1)

#descending
list2 = [1,5,6,9,7,3]
list2.sort(reverse=True)
print (list2)

#selection sort
x = [2,9,5,2,3,7,71,1]

i = 0
j = i+1
l = len(x)

while i < l:
    while j <l:
        if x[i] > x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
        j = j +1
    i = i+1
    j = i+1
print(x)

x = [2,9,5,2,3,7,71,1]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] < x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp

print (x)

#bubble sort
#ascending
x = [2,9,5,2,3,7,71,1]
l=len(x)

for i in range(l):
    for j in range(0,l-1):
        if x[j] > x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
print (x)

#descending

x = [2,9,5,2,3,7,71,1]
l=len(x)

for i in range(l):
    for j in range(0,l-1):
        if x[j] < x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            #x[j],x[j+1] = x[j+1],x[j]
print (x)

















