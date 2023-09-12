import random
from turtle import Turtle

class Maca(Turtle):
    def __init__(self):
        super(Maca, self).__init__()
        self.color('red')
        self.shape('circle')
        self.penup()
        self.shapesize(0.6)
    def nova_maca(self):
        x, y = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(x,y)
