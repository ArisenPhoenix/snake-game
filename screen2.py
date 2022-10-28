import turtle
from snake2 import Snake
from snake_variables2 import ScreenVars as Screens


SCREEN = Screens()
SCREEN_X = SCREEN.SCREEN_X
SCREEN_Y = SCREEN.SCREEN_Y
screen = turtle.Screen()


class Screen:
    def __init__(self):
        super().__init__()
        self.screen = screen
        self.screen_setup()

    def screen_setup(self):
        self.screen.listen()
        self.screen.title('Snake')
        self.screen.tracer(0)
        self.screen.bgcolor('black')
        self.screen.setup(SCREEN_X, SCREEN_Y)
        self.screen.setworldcoordinates(-SCREEN.SCREEN_SIZE_X, -SCREEN.SCREEN_SIZE_Y, SCREEN.SCREEN_SIZE_X, SCREEN.SCREEN_SIZE_Y)


    def up(self):
        self.screen.onkey(Snake.up, "Up")

    def down(self):
        self.screen.onkey(Snake.down, "Down")

    def left(self):
        self.screen.onkey(Snake.left, "Left")

    def right(self):
        self.screen.onkey(Snake.right, "Right")


    def exit_on_click(self):
        self.screen.exitonclick()
