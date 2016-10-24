from turtle import left, right, forward, shape, clear, exitonclick, penup, pendown

shape("turtle")

a = 10
for b in range(8):
    forward(a)
    penup()
    forward(a)
    pendown()
    a = a + 10

exitonclick()
