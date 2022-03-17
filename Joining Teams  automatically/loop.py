import csv
import time
import datetime
import subprocess
import pyautogui as pt
import joinmeet

def main():
    file =open('timetable.csv', mode='r')
    all_lines = csv.reader(file)
    feild=next(all_lines)
    #print(feild)
    count=0
    while True:
        d_now= datetime.datetime.now()
        year= int(d_now.strftime("%Y"))
        month=int(d_now.strftime("%m"))
        day=int(d_now.strftime("%d"))
        
        for i in feild:
            classtime=i.split(':')
            d_class = datetime.datetime(year,month,day,int(classtime[0]),int(classtime[1]),00)
            d1=d_class+datetime.timedelta(minutes =10)
            if d_now > d_class and d_now < d1:
                subprocess.run("openchrome.bat")
                time.sleep(2)
                with pt.hold('ctrl'):pt.press('w')
                x=feild.index(i)
                #print(classtime)
                feild.remove(i)
                joinmeet.main(i)
                time.sleep(600)
                count+=1
                break
        else:
            time.sleep(60)
            print("IN LOOP.py: No Class Now",datetime.datetime.now())
        if len(feild)==0:
            break

