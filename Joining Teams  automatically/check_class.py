import csv
import datetime
import time

def main(time):
    #acessing the time table
    file =open('timetable.csv', mode='r')
    all_lines = csv.reader(file)
    feild=next(all_lines)
    #feild=['8:00', '8:50', '9:50', '10:40', '11:40', '14:10', '14:50', '15:50', '16:40']
    d_now= datetime.datetime.now()
    wnum=int(d_now.strftime("%w"))
    count=0
    for i in all_lines:
        if count==wnum:
            schedule= i.copy()
            break
        count+=1
        
    for i in feild:
        if i == time:
            x=feild.index(i)
            class_now=schedule[x]
            return class_now
    else:
        class_now="None"
        return class_now

