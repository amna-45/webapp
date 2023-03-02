'''f=open("D:\web design and development\countryy.txt", "a") #append
f.write("cholistan")
f.close()
'''
'''
f=open("D:\web design and development\countryy.txt") 
d=f.read()
name=input("Enter any country name : ")
if name in d:
    print("yes")
else:
    print("no")
'''
f=open("D:\web design and development\countryy.txt", "r")

''' #read specific line
content = f.readlines()  
print("4th line")
print(content[4])
print("first three lines")
print(content[0:3])  
      OR
    '''
specified_lines = [3, 7]
for pos, l_num in enumerate(f):
	if pos in specified_lines:
		print(l_num)

