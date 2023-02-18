a=int(input("enter 1st number: "))
b=int(input("Enter second number: "))
c=int(input("Enter 3rd number: "))
d=int(input("enter 4th number: "))

if (a>b):
    max=a
else:
    max=b
if (c>d):
    max2=c
else:
    max2=d
if (max>max2):
    print("Maximum number is : ",max)
else:
    print("Maximum number is : ",max2)

n=[a,b,c,d]
print("List of numbers are: ",n)
n.sort()
print("Sorted List : ", n)