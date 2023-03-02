#read and write in csv file
import csv

f=open("D:\web design and development\python code\username.csv", "r+")
reader = csv.reader(f)
for row in reader:
    print(row)

writer = csv.writer(f)
writer.writerow(['Username', 'Identifier', 'First name','Last name'])
writer.writerow(['Ali3', 'A3', 'Alii', 'Hassan'])

f.close()

