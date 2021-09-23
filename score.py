from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Courier", 12, "normal")
FONT2 = ("Bold", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.my_score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.my_score} HIGH SCORE: {self.high_score} ", align=ALIGNMENT, font=FONT1)

    def scorecard(self):
        self.my_score += 1
        self.updateScoreboard()

    def reset(self):
        if self.my_score > self.high_score:
            self.high_score = self.my_score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.my_score = 0
        self.updateScoreboard()

    # def game_over(self):
    #     self.color("cyan")
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT2)
