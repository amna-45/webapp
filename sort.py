'''a=int(input("enter 1st number: "))
b=int(input("Enter second number: "))
c=int(input("Enter 3rd number: "))
d=int(input("enter 4th number: "))
n=[a,b,c,d]
print("List of numbers are: ",n)
n.sort()
print("Sorted List : ", n) '''

L=[]
n=1
for i in range(0,4):
    a=int(input("Enter %s number: "%(n)))
    L.append(a)
    n=n+1
print("Unsorted list: ",L)
L.sort()
print("Sorted list: ",L)
    