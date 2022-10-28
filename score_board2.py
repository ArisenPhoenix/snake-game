from turtle import Turtle
from snake2 import Snake
snake = Snake()
style = ('Courier', 20, 'italic')
big_style = ('Times New Roman', 30, 'bold')
game_over = ('Times New Roman', 50, 'italic')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.PEN = Turtle()


    def write_score(self, score_tally):
        self.PEN.penup()
        self.PEN.hideturtle()
        self.PEN.goto(0, 1800)
        self.PEN.pendown()
        self.PEN.color('deep pink')
        self.PEN.write(f'Your Score Is: {snake.score}', font=style, align='center')


    def update_score(self, score_tally):
        self.PEN.clear()
        self.PEN.write(f'Your Score Is: {snake.score}', font=style, align='center')
