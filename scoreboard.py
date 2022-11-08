from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0)]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LINE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_scoreboard()
        self.line()

    def update_scoreboard(self):
        self.clear()
        self.line()
        self.goto(-200, 200)
        self.write(self.player_1_score, align="center", font=("Arial", 70, "normal"))
        self.goto(200, 200)
        self.write(self.player_2_score, align="center", font=("Arial", 70, "normal"))

    def player_1_scored(self):
        self.player_1_score += 1
        self.update_scoreboard()

    def player_2_scored(self):
        self.player_2_score += 1
        self.update_scoreboard()

    def line(self):

        self.penup()
        self.goto(x=0, y=(SCREEN_HEIGHT / 3))
        self.setheading(DOWN)

        for i in range(int((SCREEN_HEIGHT / 3) / LINE_DISTANCE)):
            self.pendown()
            self.forward(LINE_DISTANCE)
            self.penup()
            self.forward(LINE_DISTANCE)
