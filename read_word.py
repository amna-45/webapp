#read a specific word from specific line
f=open("D:\web design and development\countryy.txt", "r")
d=f.readlines()
a=d[2]
sp=a.split() #convert line to words
#print(sp) 
print(sp[1]) #display 2nd word