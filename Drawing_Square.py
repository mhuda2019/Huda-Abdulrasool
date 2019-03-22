import lab1
a = lab1.Turtle()

a.speed(20)
color = ['red', 'green', 'yellow', 'blue']
for i in range(200):
    a.color(color[i % 4])
    a.forward(i)
    a.right(90)

lab1.done()