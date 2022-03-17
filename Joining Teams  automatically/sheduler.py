import csv 
import time
import datetime

def main():

    #getting current date and time
    date= datetime.datetime.now()
    day= date.strftime("%A")
    hour=date.strftime("%H")
    minute= date.strftime("%M")
    #calulating the day num
    #week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    wnum=int(date.strftime("%w"))
    '''for i in week:
        if i==day:
            break
        wnum+=1'''
    count=0
    for i in all_lines:
        if count==wnum:
            shedule= i.copy()
            break
        count+=1
   
    #checking the feild for class
    for i in feild:
        hr_min= i.split(':')
        if hr_min[0] == hour:
            
            if (int(hr_min[1])>= (int(minute)-15)) or (int(hr_min[1])<= (int(minute)+10)):
                x=feild.index(i)
                class_now=shedule[x]
                break
    else:
        class_now="None"

    return class_now


