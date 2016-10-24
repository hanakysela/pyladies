from turtle import left, right, forward, shape, clear, exitonclick, penup, pendown

def domecek(a):
    shape("turtle")

    left(90)
    forward(a)
    right(90)
    forward(a)
    left(135)
    forward(((a**2)/2)**(1/2))
    left(90)
    forward(((a**2)/2)**(1/2))
    left(90)
    forward((2*(a**2))**(1/2))
    left(135)
    forward(a)
    left(135)
    forward((2*(a**2))**(1/2))
    left(135)
    forward(a)




#exitonclick()
#return
