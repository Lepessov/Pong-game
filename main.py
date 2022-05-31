import time

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

screen = Screen()
ball = Ball()
l = Paddle(-350)
r = Paddle(350)
score = ScoreBoard()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong game')
screen.tracer(0)

screen.listen()
screen.onkey(r.up, 'Up')
screen.onkey(r.down, 'Down')
screen.onkey(l.up, 'w')
screen.onkey(l.down, 's')


game = True

while game:
    time.sleep(ball.get_speed())
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.xcor() > 450:
        score.add_r()
        ball.reset()

    if ball.xcor() < -450:
        score.add_l()
        ball.reset()

    if ball.distance(r) < 50 and ball.xcor() > 290:
        ball.bounce_x()

    if ball.distance(l) < 50 and ball.xcor() < -290:
        ball.bounce_x()





screen.exitonclick()
