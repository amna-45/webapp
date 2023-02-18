m1=int(input("Enter your 1st subject marks: "))
m2=int(input("Enter 2nd subject marks: "))
m3=int(input("enter 3rd subject marks: "))
avg=int((m1+m2+m3)/3)
if (m1<33 or m2<33 or m3<33):
    print("Opss Your are fail, your marks are less than 33 ")
elif (avg<40):
    print("You are fail , as average is less than 40")
else:
    print("Congratulations You are pass")