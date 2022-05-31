from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
       super().__init__() 
       self.color('white')
       self.ht()
       self.penup()
       self.goto(0, 260)
       self.r_score = 0
       self.l_score = 0
       self.show_score()

    def show_score(self):
        self.write(f'{self.r_score}  {self.l_score}', align='center', font=('Arial', 30, 'normal'))

    def add_r(self):
        self.clear()
        self.r_score += 1
        self.show_score()

    def add_l(self):
        self.clear()
        self.l_score += 1
        self.show_score()
