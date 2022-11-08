import turtle
from turtle import colormode, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from computer import Computer
import time
game_is_on = True
colormode(255)
LEVEL = turtle.numinput(title="difficulty", prompt="Choose a level 1-3.")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STARTING_POSITION = [((-1 * (SCREEN_WIDTH/2)) + 50, 0), ((SCREEN_WIDTH/2) - 50, 0)]
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((STARTING_POSITION[1]))
computer_paddle = Computer((STARTING_POSITION[0]))
scoreboard = Scoreboard()

ball = Ball()

screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeypress(key='Down', fun=r_paddle.down)

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    computer_paddle.play(ball.ycor(), level=LEVEL)
    screen.listen()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 365:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.player_1_scored()
    if ball.xcor() < -365:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.player_2_scored()

    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(computer_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
