from turtle import *
sc=Screen()
sc.listen()
def movefd():
    fd(100)
def movebk():
    bk(100)
def moveleft():
    left(90)
def moveright():
    right(90)

sc.onkey(movefd,'A')
sc.onkey(movebk,'Down')
sc.onkey(moveleft,'Left')
sc.onkey(moveright,'Right')
done()