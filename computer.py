from turtle import Turtle
import operator
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STARTING_POSITION = [((-1 * (SCREEN_WIDTH/2)) + 50, 0), ((SCREEN_WIDTH/2) - 50, 0)]
operations = {"+": operator.add, "-": operator.sub}


class Computer(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")
        self.goto(position)

    # def play(self):
    #     if 300 > self.ycor() > -300:
    #         new_y = random.choice(list(operations.values()))(self.ycor(), random.randrange(100))
    #         self.goto(self.xcor(), new_y)
    #     else:
    #         self.goto(STARTING_POSITION[0])
    def play(self, ball_ycor, level):
        rand_num = random.randrange(1, 10)
        if level == 1:

            if rand_num in (1, 2, 3, 4, 5, 6):
                new_y = ball_ycor - 70
                self.goto(self.xcor(), new_y)
            elif rand_num in (7, 8):
                new_y = ball_ycor - 54
                self.goto(self.xcor(), new_y)
            elif rand_num in (9, 10):
                new_y = ball_ycor
                self.goto(self.xcor(), new_y)
        elif level == 2:
            if rand_num in (1, 2, 3, 4):
                new_y = ball_ycor - 70
                self.goto(self.xcor(), new_y)
            elif rand_num in (5, 6):
                new_y = ball_ycor - 54
                self.goto(self.xcor(), new_y)
            elif rand_num in (7, 8, 9, 10):
                new_y = ball_ycor
                self.goto(self.xcor(), new_y)
        elif level == 3:
            if rand_num in (1, 2, 3):
                new_y = ball_ycor - 70
                self.goto(self.xcor(), new_y)
            elif rand_num in (4, 5, 6, 7, 8, 9, 10):
                new_y = ball_ycor
                self.goto(self.xcor(), new_y)
