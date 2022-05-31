from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, tups):
        self.tups = tups
        super().__init__()
        self.create()

    def create(self):
       self.color('white')
       self.shape('square')
       self.shapesize(stretch_wid=6, stretch_len=1)
       self.turtlesize(stretch_wid=6, stretch_len=1)
       self.penup()
       self.goto(self.tups, 0)
       self.speed('fastest')
        
    def up(self):
        self.goto(self.xcor(), self.ycor() + 20) 


    def down(self):
        self.goto(self.xcor(), self.ycor() - 20) 
