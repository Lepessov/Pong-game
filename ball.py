from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
       self.color('white')
       self.shape('circle')
       self.shapesize(stretch_wid=1, stretch_len=1)
       self.penup()
       self.goto(0, 0)
       self.x_move = 10
       self.y_move = 10
       self.move_speed = 0.01

 
    def move(self):
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()

    def get_speed(self):

        return self.move_speed

