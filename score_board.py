from turtle import Turtle
import snake_variables

snakes = snake_variables
screens = snakes.ScreenVars()
style = ('Courier', 20, 'italic')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as previous_high_score:
            self.high_score = int(previous_high_score.read())
        self.difference = 0


    def add_score(self, num):
        last_score = self.score
        self.score += num
        self.difference = self.score - last_score
        return self.difference


    def what_is_score(self):
        return self.score


    def write_score(self):
        self.hideturtle()
        self.penup()

        self.goto(-screens.SCREEN_SIZE_X*.8, screens.SCREEN_SIZE_Y*.90)
        self.color('deep pink')
        self.write(f'Score: {self.score}', font=style, align='center')

    def write_scores(self):
        self.clear()
        self.write_score()
        self.write_high_score()


    def write_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.hideturtle()
        self.penup()

        self.goto(screens.SCREEN_SIZE_X*.7, screens.SCREEN_SIZE_Y*.90)
        self.color('deep pink')
        self.write(f'High Score: {self.high_score}', font=style, align='center')

    def reset_score(self):
        self.score = 0


    def save_high_score(self):
        with open('data.txt', mode='w') as new_high_score:
            new_high_score.write(f'{self.high_score}')

