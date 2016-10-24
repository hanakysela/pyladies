from turtle import left, right, forward, shape, clear, exitonclick, penup, pendown

shape("turtle")

penup()
left(180)
forward(500)
left(180)
pendown()


for i in range(10):

    left(90)
    forward(100)
    right(90)
    forward(100)
    left(135)
    forward((5000)**(1/2))
    left(90)
    forward((5000)**(1/2))
    left(90)
    forward(20000**(1/2))
    left(135)
    forward(100)
    left(135)
    forward(20000**(1/2))
    left(135)
    forward(150)




exitonclick()
