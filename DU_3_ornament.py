from turtle import left, right, forward, shape, clear, exitonclick, penup, pendown

shape("turtle")

a = 5
for b in range(36):
    forward(a)
    left(45)
    a=a+2
exitonclick()
