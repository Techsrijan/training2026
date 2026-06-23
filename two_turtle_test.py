from turtle import *

# Create turtles
t1 = Turtle()
t2 = Turtle()

# Move forward function
def movefd():
    t1.pencolor('red')
    t1.fd(100)

# Move backward function
def movebk():
    t2.pencolor('blue')
    t2.fd(200)

# Movement functions for keys
def moveleft():
    t1.left(90)

def moveright():
    t1.right(90)

# Setup screen and listen for events
sc = Screen()
sc.listen()

# Bind keys to functions
sc.onkey(movefd, 'A')
sc.onkey(movebk, 'Down')
sc.onkey(moveleft, 'Left')
sc.onkey(moveright, 'Right')

# Keep the window open
done()
