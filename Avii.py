from turtle import*
t=Turtle()
t.speed(0)
color = ["red", "green", "blue", "yellow", "cyan", "magenta"]
for i in range(500):
        t.pencolor(color[i%5])
        t.forward(i*10)
        t.left(145)
mainloop()