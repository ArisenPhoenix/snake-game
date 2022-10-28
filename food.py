from turtle import Turtle
import time
from snake_variables import SnakeVars as Snakes
from snake_variables import GameVars as Games
from snake_variables import FoodVars as Foods
import random
Foods = Foods()
FOODS = Foods.food
SNAKES = Snakes()
GAMES = Games()

FOOD_SIZE = Foods.FOOD_SIZE
DISTANCE = Foods.DISTANCE


class Food:
    def __init__(self):
        self.food = FOODS
        self.create_food()
        self.create_special_food()
        self.start_time = 0
        self.end_time = 0

    #
    def create_food(self):
        self.food.append(Turtle(visible=False))
        self.food[0].shape('circle')
        self.food[0].penup()
        self.food[0].color('green')
        self.food[0].shapesize(FOOD_SIZE)
        self.food[0].goto(random.randint(-DISTANCE, DISTANCE), random.randint(-DISTANCE, DISTANCE))
        self.food[0].showturtle()


    def create_special_food(self):
        self.food.append(Turtle(visible=False))
        self.food[1].shape('circle')
        self.food[1].penup()
        self.food[1].color('red')
        self.food[1].shapesize(FOOD_SIZE)
        self.food[1].goto(random.randint(3*-DISTANCE, 3*DISTANCE), random.randint(3*-DISTANCE, 3*DISTANCE))


    def special_food_unavailable(self):
        self.food[1].hideturtle()
        self.food[1].goto(3*-DISTANCE, 3*DISTANCE)


    def special_food_available(self):
        self.food[1].goto(random.randint(int(.8*-DISTANCE), int(.8*DISTANCE)), random.randint(int(.8*-DISTANCE), int(.8*DISTANCE)))
        self.food[1].showturtle()


    def food_time_start(self):
        self.start_time = time.time()
        return self.start_time

    def food_time_end(self):
        self.end_time = time.time()
        return self.end_time


    def move_food(self):
        self.food[0].hideturtle()
        self.food[0].goto(random.randint(-DISTANCE, DISTANCE), random.randint(-DISTANCE, DISTANCE))
        self.food[0].showturtle()
