import turtle


t = turtle.Turtle()

s = turtle.Screen()
colors = ['orange', 'red', 'green', 'blue', 'cyan', 'yellow', 'purple', 'magenta', 'light blue']

s.bgcolor('black')
t.pensize(2)
t.speed(0)
for i in range(360):
    t.pencolor(colors[i % 7])
    t.width(i//100+1)
    t.forward(i)
    t.right(59)
    turtle.hideturtle()
