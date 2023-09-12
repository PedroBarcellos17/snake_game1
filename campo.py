from turtle import Turtle

class Campo(Turtle):
    def __init__(self):
        super(Campo, self).__init__()
        self.penup()
        self.pensize(4)
        self.goto(285, 285)
        self.pendown()
        self.goto(285, -285)
        self.goto(-285, -285)
        self.goto(-285, 285)
        self.goto(285, 285)
        self.hideturtle()