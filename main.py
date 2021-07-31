from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=800, width=800)
screen.bgcolor("black")
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)   # width is 5 x default ie 5 x 20 & len is 20
paddle.penup()
paddle.goto(350, 0)

screen.exitonclick()
