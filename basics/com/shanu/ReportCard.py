print("**Report Card**")
studentname = str(input("Student Name: "))
English = int(input("English Marks "))
Hindi = int(input("Hindi Marks "))
Maths = int(input("Maths Marks "))
Science = int(input("Science Marks "))
Computer = int(input("Computer Marks "))
EVS = int(input("EVS Marks "))
Total = English + Hindi + Maths + Science + Computer + EVS
print ("Total Marks of",studentname , "=", Total)
percentage = (Total/600)*100
if percentage <= 30:
    print("Fail")
elif percentage < 60:
    print ("Grade C")
elif percentage < 75:
    print ("Grade B")
else:
    print ("Grade A")

