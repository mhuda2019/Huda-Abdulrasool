import turtle

ob = turtle.Turtle()

ob.speed(20)
ob.getscreen().bgcolor("pink")
ob.color("red")

def circle(z, l, c):
    ob.lt(z)
    ob.fd(l)
    ob.rt(90)
    ob.color(c)
    ob.begin_fill()
    ob.circle(40)
    ob.end_fill()
    ob.home()


circle(110, 50, "yellow")
circle(70, 50, "green")
circle(98, 195, "orchid")
circle(85, 135, "cyan")

turtle.done()

