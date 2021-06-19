import datetime

f = open("data.txt", 'a')

x=datetime.datetime.now()
year = str(x.year)

month=input("Enter the month (In number) : ")
day=input("Enter the day : ")
name=input("Enter name : ")
phn=input("Enter phone number (With STD code) : ")

while len(phn) != 13:
    print("Invalid phone number!")
    phn=input("Enter phone number (With STD code) : ")

data = day + "-" + month + "-" + year + "-" + name + "-" + phn + "-" + '\n'

f.write(data)
f.close