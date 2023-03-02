sum=0
try:
    a=int(input('Enter 1st number '))
    b=int(input('2nd number '))
    sum=a+b
except Exception as e:
    print(e)
print(sum)