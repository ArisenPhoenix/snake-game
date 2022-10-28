import turtle
from turtle import Turtle
from screen2 import Screen
from food2 import Food
from snake2 import Snake
from score_board2 import ScoreBoard
from snake_variables2 import GameVars as Games
from snake_variables2 import SnakeVars as Snakes
from snake_variables2 import FoodVars as Foods
from snake_variables2 import ScreenVars as Screens
import time
# from snake_variables2 import ScreenVars as Screens
# Screens = Screens()
# screen.listen()
# screen.onkey(Snake.up, "Up")
# screen.onkey(Snake.down, "Down")
# screen.onkey(Snake.left, "Left")
# screen.onkey(Snake.right, "Right")
# screen.title('Snake')
# screen.bgcolor('black')
# screen.tracer(0)
# screen.setup(SCREEN.SCREEN_X, SCREEN.SCREEN_Y)
# screen.setworldcoordinates(-SCREEN.SCREEN_SIZE_X, -SCREEN.SCREEN_SIZE_Y, SCREEN.SCREEN_SIZE_X, SCREEN.SCREEN_SIZE_Y)
PEN = ScoreBoard()
SCREEN = Screens()
screen = Screen()
# screen.title('Snake')
# screen.bgcolor('black')
# screen.tracer(0)
# screen.setup(SCREEN.SCREEN_X, SCREEN.SCREEN_Y)
# screen.setworldcoordinates(-SCREEN.SCREEN_SIZE_X, -SCREEN.SCREEN_SIZE_Y, SCREEN.SCREEN_SIZE_X, SCREEN.SCREEN_SIZE_Y)

FOODS = Foods()
GAMES = Games()
SNAKES = Snakes()

Food = Food()
Snake = Snake()
snake = Snake.snake
head = Snake.head
food = Food.food

style = ('Courier', 20, 'italic')
big_style = ('Times New Roman', 30, 'bold')
game_over = ('Times New Roman', 50, 'italic')

# screen.listen()
# screen.onkey(Snake.up, "Up")
# screen.onkey(Snake.down, "Down")
# screen.onkey(Snake.left, "Left")
# screen.onkey(Snake.right, "Right")

PEN.left(90)
PEN.forward(1800)
going = True
start = 0


def compare_coordinates():
    global start
    for foods in range(len(food)):
        if head.distance(food[foods].xcor(), food[foods].ycor()) <= SNAKES.MOVE_DISTANCE:
            if foods == 0:
                Snake.add_score(1)
                PEN.write_score(Snake.score)
                Snake.increase_speed(True)

                if Snake.special_tally():
                    Food.special_food_available()
                    start = Food.food_time_start()

                Food.move_food()
                Snake.add_snake()
            if foods == 1:
                Snake.add_score(8)
                PEN.write_score(Snake.score)
                Snake.increase_speed(True)
                Snake.add_snake()
                if head.distance(food[1].xcor(), food[1].ycor()) <= SNAKES.MOVE_DISTANCE:
                    Food.special_food_unavailable()
        Food.food_time_end()
        if Food.food_time_end() - start >= 5:
            Food.special_food_unavailable()


def write_game_over():
    PEN.update_score(Snake.score)
    PEN.right(180)
    PEN.forward(1400)
    time.sleep(.02)
    PEN.color('deep pink')
    PEN.write(f'Your Score Is: {Snake.score}', font=style, align='center')
    PEN.forward(400)
    PEN.right(180)
    PEN.write(f'---- GAME OVER ----', font=game_over, align='center')


# def retry():
#     decision = screen.textinput('Play Again?', '(y) for YES, (n) for NO.')
#     if decision.lower() == 'y' or decision.lower() == 'yes':
#         print('Ok Let The Fun Begin')
#         screen.bye()
#         game_start()


def is_game_over():
    if game_is_over():
        PEN.update_score(Snake.score)
        write_game_over()


def game_is_over():
    for segment in range(1, len(snake)):
        seg = snake[segment]
        if head.distance(seg.xcor(), seg.ycor()) < SNAKES.MOVE_DISTANCE*.999:
            if seg.distance(head.xcor(), head.ycor()) < SNAKES.MOVE_DISTANCE*.999 and seg.pos() != seg.home():
                PEN.update_score(Snake.score)
                global going
                going = False
                return True
        if head.xcor() >= GAMES.SQUARE_DIMENSIONS or head.xcor() <= -GAMES.SQUARE_DIMENSIONS:
            print(f'Collision at X: {head.xcor()}')
            going = False
            return True


def game_go():
    Snake.move()
    screen.update(Snake.score)
    compare_coordinates()
    is_game_over()
    if game_is_over():
        print(f'Your Final Score Is: {Snake.score}')


def game_start():
    PEN.write_score(Snake.score)
    while going:
        time.sleep(Snake.speed)
        game_go()


game_start()

screen.exitonclick()
