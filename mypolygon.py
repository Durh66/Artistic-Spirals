import turtle
bob=turtle.Turtle()
s = turtle.Screen()
bob.pencolor("light blue")
s.bgcolor("black")
bob.speed(15)
def circle( t,raduis):
    for i in range(10):
        t.circle(raduis)
        raduis=raduis-4   
def design(t):
    for i in range(10):
        circle(t,150)
        t.right(36)
design(bob)
turtle.mainloop()





