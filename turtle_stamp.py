from turtle import *
from time import *
speed(1)
shape('turtle')
color('red','black')
pu()
goto(30,30)
s=10

for i in range(50):
    s=s+2
    pd()
    stamp()
    pu()
    fd(s)
    right(25)
    sleep(0.25)


done()