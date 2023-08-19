from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'bold')


class Playagain(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.hideturtle()

    def create_option(self):
        options = ["Press 'p' to Play again", "Press 'e' to Exit"]
        pos = [(0, -25), (0, -50)]
        for i in range(2):
            self.goto(pos[i])
            self.write(arg=options[i], move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def pause(self):
        self.goto(0, 50)
        self.write("PLAY", move=False, align=ALIGNMENT, font=FONT)



