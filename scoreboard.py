from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        with open("hiscore.txt") as hscore:
            self.hiscore = int(hscore.read())
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  Highscore: {self.hiscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.hiscore:
            with open("hiscore.txt", "w") as hs:
                    hs.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


