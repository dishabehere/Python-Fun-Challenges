from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.speed("fastest")
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)