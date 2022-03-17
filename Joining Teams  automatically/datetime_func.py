import datetime

d1 = datetime.datetime(2020, 5, 13, 22, 50, 55) 


now = datetime.datetime.now()
after_10_min = now + datetime.timedelta(minutes = 10)

x = datetime.datetime.now()
t=x.strftime("%X")
print(type(t)) 

