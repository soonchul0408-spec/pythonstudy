import turtle

s = turtle.Screen()
s.setup(width=800, height=600)

t = turtle.Turtle()
t.circle(100)
t.penup()
t.goto(-40, 130)
t.dot(15)
t.goto(40, 130)
t.dot(15)
t.goto(-40, 60)
t.pendown()
t.right(90)
t.circle(40, 180)



turtle.done()