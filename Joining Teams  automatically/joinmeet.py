import pyautogui as pt
import time
import datetime
import check_class

#loacting join button 
def locate(loc):
    pos=pt.locateOnScreen(loc, confidence=0.7)
    point=pt.center(pos)
    x=point[0]
    y=point[1]
    pt.click(x,y)

def jointeam(class_now):  
    #filter in teams
    with pt.hold(['ctrl','shift']):pt.press('3')
    time.sleep(2)
    try:
        locate('end.png')
    except TypeError:
        with pt.hold(['ctrl','shift']):pt.press('3')
    with pt.hold(['ctrl','shift']):pt.press('f')
    time.sleep(1)
    pt.write(class_now) #team name
    pt.press('enter')
    time.sleep(2)
    #pt.click(x=158, y=267)
    try:
        locate("general.png")
    except TypeError:
        locate("general_bold.png")
    time.sleep(2)
    

    def mic():
        pos=pt.locateOnScreen("toogle_on.png", confidence=0.7)
        if pos is None:
            time.sleep(1)
            locate("join2.png")
        else:
            locate("toogle_on.png")
            time.sleep(1)
            locate("join2.png")

    def join():
        global count
        try:
            locate("join.png")
            time.sleep(2)
            mic()
            
        except TypeError:
            count+=1
            time.sleep(20)
            if count>5:
                with pt.hold('ctrl'): pt.press('r')
                count=0
                time.sleep(20)
                jointeam(class_now)
            else:
                join()
                
    join()

count=0
def main(time):
    #class now
    class_now=check_class.main(time)
    if class_now=="None":
        #pt.alert(text="No Class Now", title="Scheduler")
        print("IN JOINMEET.py: Free Hour",datetime.datetime.now())
    else:
        jointeam(class_now)
   
