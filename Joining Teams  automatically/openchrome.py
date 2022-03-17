import subprocess
import time
def main():
    subprocess.run("openchrome.bat")
    time.sleep(25)

"""
import pyautogui as pt
import time

pt.FAILSAFE= False
#loacting join button 
def locate(loc):
    pos=pt.locateOnScreen(loc, confidence=0.7)
    point=pt.center(pos)
    x=point[0]
    y=point[1]
    pt.click(x,y)

def main():
    with pt.hold('win'): pt.press('d')
    #refresh
    for i in range(2):
        time.sleep(1)
        pt.click(x=860, y=98, button='right')
        pt.click(x=916, y=163)
    #opening chrome
    time.sleep(1)
    locate("chrome.png")
    #pt.click(x=37, y=265) #co-ordinates of chrome extension
    pt.press('enter')
    time.sleep(20)
    #open whatsapp and teams
    pt.write('https://teams.microsoft.com/') 
    pt.press('enter')    
    time.sleep(10)
    with pt.hold('ctrl'): pt.press('t')
    time.sleep(5)
    pt.write('https://web.whatsapp.com/') 
    pt.press('enter') 
    time.sleep(10)
    with pt.hold('ctrl'): pt.press('tab')
    time.sleep(10)
"""





    

