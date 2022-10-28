from turtle import Turtle
PEN = Turtle().pen()
COORDS = [(0, 0), (-500, 0)]
MOVE_DISTANCE = 120
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
HEAD_SIZE = 3
SPEED = .10
Score = 0


class GameVars:
    def __init__(self):
        self.SQUARE_DIMENSIONS = 2100
        self.SCREEN_SIZE_X = self.SQUARE_DIMENSIONS
        self.SCREEN_SIZE_Y = self.SQUARE_DIMENSIONS
        self.PIXEL_PITCH = 0.282  # mm
        self.MM_PER_INCH = 25.4
        self.DOTS_PER_INCH = int(1 / (self.PIXEL_PITCH / self.MM_PER_INCH))
        self.SPEED = SPEED
        self.SCORE = Score


    def game_vars(self):
        self.SQUARE_DIMENSIONS = 2100
        self.SCREEN_SIZE_X = self.SQUARE_DIMENSIONS
        self.SCREEN_SIZE_Y = self.SQUARE_DIMENSIONS
        self.PIXEL_PITCH = 0.282  # mm
        self.MM_PER_INCH = 25.4
        self.DOTS_PER_INCH = int(1 / (self.PIXEL_PITCH / self.MM_PER_INCH))
        self.SPEED = SPEED
        self.SCORE = Score


class SnakeVars:
    def __init__(self):
        self.COORDS = [(0, 0), (-500, 0), (-1000, 0)]
        self.MOVE_DISTANCE = MOVE_DISTANCE
        self.UP = UP
        self.DOWN = DOWN
        self.LEFT = LEFT
        self.RIGHT = RIGHT
        self.HEAD_SIZE = 3


    def snake_vars(self):
        self.COORDS = [(0, 0), (-500, 0), (-1000, 0)]
        self.MOVE_DISTANCE = MOVE_DISTANCE
        self.UP = UP
        self.DOWN = DOWN
        self.LEFT = LEFT
        self.RIGHT = RIGHT
        self.HEAD_SIZE = 3


class FoodVars:
    def __init__(self):
        self.food = []
        self.SEEN = True
        self.FOOD_SIZE = HEAD_SIZE/2
        self.DISTANCE = 1100

    def food_vars(self):
        self.food = []
        self.SEEN = True
        self.FOOD_SIZE = HEAD_SIZE/2
        self.DISTANCE = 1100


class ScreenVars:
    def __init__(self):
        self.SQUARE_DIMENSIONS = 2100
        self.SCREEN_SIZE_X = self.SQUARE_DIMENSIONS
        self.SCREEN_SIZE_Y = self.SQUARE_DIMENSIONS
        self.PIXEL_PITCH = 0.282  # mm
        self.MM_PER_INCH = 25.4
        self.DOTS_PER_INCH = int(1 / (self.PIXEL_PITCH / self.MM_PER_INCH))
        self.SCREEN_X = 13 * self.DOTS_PER_INCH
        self.SCREEN_Y = 13 * self.DOTS_PER_INCH

    def screen_vars(self):
        self.SQUARE_DIMENSIONS = 2100
        self.SCREEN_SIZE_X = self.SQUARE_DIMENSIONS
        self.SCREEN_SIZE_Y = self.SQUARE_DIMENSIONS
        self.PIXEL_PITCH = 0.282  # mm
        self.MM_PER_INCH = 25.4
        self.DOTS_PER_INCH = int(1 / (self.PIXEL_PITCH / self.MM_PER_INCH))
        self.SCREEN_X = 13 * self.DOTS_PER_INCH
        self.SCREEN_Y = 13 * self.DOTS_PER_INCH
