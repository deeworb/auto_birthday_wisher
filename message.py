import pywhatkit as kit
import datetime
import os
import time

names = []

with open("data.txt", 'r') as f:

    with open("temp.txt", 'a') as f2:

        f1 = f.readlines()

        for x in f1:
            data = x.split('-')
            day = int(data[0])
            month = int(data[1])
            year = int(data[2])
            name = data[3]
            num = data[4]
            today = datetime.datetime.now()

            if int(today.day)==day and int(today.month)==month and int(today.year)==year:
                kit.sendwhatmsg_instantly(num, "Happy Birthday "+name, wait_time=5)
                year = year + 1
                data = str(day) + "-" + str(month) + "-" + str(year) + "-" + name + "-" + num + "-" + '\n'
                f2.write(data)
                print("Birthday wished for", name)
                time.sleep(3)

            else:
                data = str(day) + "-" + str(month) + "-" + str(year) + "-" + name + "-" + num + "-" + '\n'
                f2.write(data)
                
os.remove("data.txt")
os.rename("temp.txt", "data.txt")