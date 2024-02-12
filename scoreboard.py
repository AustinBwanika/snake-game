from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()

    def set_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", move=False, font=('Courier', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", move = False, font=('Courier', 16, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
