import turtle

turtle.bgcolor("green")
turtle.pensize(10)
turtle.speed(1)


def square():
    # Square
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

square()
turtle.circle(300)
square()
turtle.forward(200)
square()
turtle.forward(300)
square()
turtle.forward(300)


turtle.hideturtle()
