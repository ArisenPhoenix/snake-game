from turtle import Turtle
from snake_variables2 import GameVars as Games
from snake_variables2 import SnakeVars as Snakes
from snake_variables2 import FoodVars as Foods
import random

SNAKES = Snakes()
GAMES = Games()
FOODS = Foods()


class Snake:
    def __init__(self):
        self.snake = []
        self.head = Turtle('square')
        self.HEADING = self.head.heading()
        self.up()
        self.down()
        self.left()
        self.right()
        self.COORDS = SNAKES.COORDS
        self.score = 0
        self.speed = GAMES.SPEED
        self.move_distance = SNAKES.MOVE_DISTANCE
        self.head_size = SNAKES.HEAD_SIZE
        self.create_head()
        self.create_snake()
        self.difference = 0
        self.tally = 0


    def create_head(self):
        self.head = Turtle('square')
        self.HEADING = self.head.heading()
        self.head.shapesize(self.head_size)
        self.head.penup()
        self.head.color('red')
        self.head.goto(SNAKES.COORDS[0])
        self.snake.append(self.head)


    def create_snake(self):
        for coord in range(1, len(self.COORDS)):
            segment = Turtle("square")
            segment.setheading(self.HEADING)
            segment.color('white')
            segment.shapesize(self.head_size*(2/3))
            segment.penup()
            segment.goto(self.COORDS[coord])
            self.snake.append(segment)


    def add_snake(self):
        if self.score == 1:
            self.difference = 1
        for i in range(self.difference):
            add_on = Turtle("square")
            add_on.penup()
            add_on.shapesize(2.5)
            add_on.goto(self.snake[-1].xcor()-self.head_size, self.snake[-1].ycor()-self.head_size)
            self.snake.append(add_on)
            add_on.setheading(self.HEADING)
            add_on.color('white')


    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            self.snake[seg].setheading(self.HEADING)
            if seg != 1:
                self.snake[seg].shapesize(SNAKES.HEAD_SIZE*.85)
            x = self.snake[seg - 1].xcor()
            y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(x, y)
        if self.snake[-1]:
            self.snake[-1].shapesize(SNAKES.HEAD_SIZE/3)
        self.head.forward(self.move_distance)


    def increase_speed(self, increment):
        num = 3
        SPEED = .10
        if increment:
            if self.score % num == 0:
                times = self.score / num
                for _ in range(int(times)):
                    SPEED -= .002
                self.speed = round(1000*SPEED, 4)
                self.speed = SPEED
                speed = 100 - round(1000*self.speed, 4)
                print(f'Speed is now: {speed}!')


    def add_score(self, num):
        last_score = self.score
        self.score += num
        self.difference = self.score - last_score
        return self.difference


    def what_is_score(self):
        return self.score


    def up(self):
        if self.head.heading() != SNAKES.DOWN:
            self.head.setheading(SNAKES.UP)


    def down(self):
        if self.head.heading() != SNAKES.UP:
            self.head.setheading(SNAKES.DOWN)


    def left(self):
        if self.head.heading() != SNAKES.RIGHT:
            self.head.setheading(SNAKES.LEFT)


    def right(self):
        if self.head.heading() != SNAKES.LEFT:
            self.head.setheading(SNAKES.RIGHT)


    def go_to_location(self, num, num2):
        self.head.goto((num, num2))


    def special_tally(self):
        self.tally += 1
        rand = random.randint(7, 15)
        if self.tally >= 7:
            decide = self.score % self.tally
            if decide == 0:
                self.tally = 0
                return True
