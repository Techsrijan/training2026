from turtle import *


t = Turtle()
wn = Screen()
wn.title("drow using mouse")
t.pencolor("red")
t.speed(-1)

#ondrag is used to bind the function to mouse event
# creating function
def paint(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(paint)

def erase(x,y):
    t.clear()


def main():
    wn.listen()
    t.ondrag(paint)
    wn.onscreenclick(erase,3)
    done()
main()