from turtle import left, right, forward, shape, clear, exitonclick, penup, pendown

n = int(input("Zadej cilo:"))
print(n)
shape("turtle")
for i in range(int(n)):
    forward(200/n)
    left(180-(180*(1-2/n)))

exitonclick()
