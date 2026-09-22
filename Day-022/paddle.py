from turtle import Turtle
seg = Turtle()
gogo = (350, -350)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        ney_y = self.ycor() + 20
        self.goto(self.xcor(), ney_y)

    def go_down(self):
        ney_y = self.ycor() - 20
        self.goto(self.xcor(), ney_y)