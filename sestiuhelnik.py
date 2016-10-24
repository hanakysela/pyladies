from turtle import left, right, forward, shape, clear, exitonclick, penup, pendown

shape("turtle")

for ul in range(6):
    for strana in range(6):
        forward(100)
        left(60)

    forward(100)
    right(60)

exitonclick()
