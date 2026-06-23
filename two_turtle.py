from turtle import *
t1=Turtle()
t2=Turtle()
sc=Screen()
sc.listen()
def movefd():
    t1.pencolor('red')
    t1.fd(100)
def movebk():
    t2.pencolor('blue')
    t2.fd(200)
# def moveleft():
#     left(90)
# def moveright():
#     right(90)

sc.onkey(movefd,'A')
sc.onkey(movebk,'Down')
# sc.onkey(moveleft,'Left')
# sc.onkey(moveright,'Right')
done()