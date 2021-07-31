from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=800, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)   # width is 5 x default ie 5 x 20 & len is 20
paddle.penup()
paddle.goto(350, 0)
screen.update()


def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()      # screen will listen to commands such as keystrokes
screen.onkey(move_up, "up")
screen.onkey(move_down, "down")


screen.exitonclick()
