# Hello World program in Python

print ("Hello World!\n")

# Hello World program in Python

print ("Hello World!")

#if product is >1000 print the sum else product

x=50
y=20
z=x*y
if z > 1000:
    print ("the sum is",x+y)
else:
    print ("the product is",z)

#print the sum of previous and current number from a list

mylist = [1,2,2,4,5,6,7,8,9,10]
previousnum = 0
for i in mylist:
    sum1 = previousnum + i
    print (sum1)
    previousnum = i

#print numbers divisible by 5 from the list

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


# find the largest value

mylist = [5,15,100,4,9]

print ("maximun number is", max(mylist))
print ("minimun number is", min(mylist))

# average of numbers in a list

mylist = [2,6,8,5,2,5,10,20]
average = sum(mylist)/len(mylist)
print ("average is", average)


# find the largest value

mylist = [5,15,100,4,9,5000]
largest = mylist[0]
for x in mylist:
    if x > largest:
        largest = x
print ("largest number is", largest)

# average of numbers in a list

mylist = [2,6,8,5,2]
sum = 0
for x in mylist:
    sum = sum + x
average = sum/ len(mylist)
print ("average is", average)

#starlist = [1,2,3,4,5,6]
#index = 10;
for x in range(1,6):
    print ('*'*x)

x=1
while x <=6:
    print ('*'*x)
    x=x+1

x=6
while x >=0:
    print ('*'*x)
    x=x-1

x=1
y=5
while x <=11:
    print (" " *y, '*'*x)
    x=x+2
    y=y-1

x=11
y=0
while x >=0:
    print (" " *y, '*'*x)
    x=x-2
    y=y+1
