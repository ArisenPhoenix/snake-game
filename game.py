from turtle import Turtle, Screen
from snake import Snake
from food import Food
from snake_variables import GameVars, ScreenVars, SnakeVars, FoodVars
import score_board
import time
rules = input('Boundaries? (b), No Boundaries (n)')
SCREEN = ScreenVars()
screen = Screen()
screen.title('Snake')
screen.bgcolor('black')
screen.tracer(0)
screen.setup(SCREEN.SCREEN_X, SCREEN.SCREEN_Y)
screen.setworldcoordinates(-SCREEN.SCREEN_SIZE_X, -SCREEN.SCREEN_SIZE_Y, SCREEN.SCREEN_SIZE_X, SCREEN.SCREEN_SIZE_Y)


SCORE = score_board.Score()


FOODS = FoodVars()
GAMES = GameVars()
SNAKES = SnakeVars()

Food = Food()
Snake = Snake()
snake = Snake.snake
head = Snake.head
food = Food.food
PEN = Turtle()

style = ('Courier', 20, 'italic')
big_style = ('Times New Roman', 30, 'bold')
game_over = ('Times New Roman', 50, 'italic')

screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")

PEN.left(90)
PEN.forward(1800)
going = True
start = 0


def no_boundaries():
    if head.xcor() < -GAMES.SQUARE_DIMENSIONS:
        head.goto(-1 * head.xcor() - 120, head.ycor())
    elif head.xcor() > GAMES.SQUARE_DIMENSIONS:
        head.goto(-1 * head.xcor() + 120, head.ycor())

    elif head.ycor() < -GAMES.SQUARE_DIMENSIONS:
        head.goto(head.xcor(), -1 * head.ycor() - 120)
    elif head.ycor() > GAMES.SQUARE_DIMENSIONS:
        head.goto(head.xcor(), -1 * head.ycor() + 120)


def boundaries():
    if head.xcor() == 5000:
        pass
    elif head.xcor() >= GAMES.SQUARE_DIMENSIONS or head.xcor() <= -GAMES.SQUARE_DIMENSIONS:
        print(f'Collision at X: {head.xcor()}')
        return True
    elif head.ycor() >= GAMES.SQUARE_DIMENSIONS or head.ycor() <= -GAMES.SQUARE_DIMENSIONS:
        print(f'Collision at Y: {head.ycor()}')
        return True


def compare_food_coordinates():
    global start
    for foods in range(len(food)):
        if head.distance(food[foods].xcor(), food[foods].ycor()) <= SNAKES.MOVE_DISTANCE:

            if foods == 0:
                SCORE.add_score(1)
                SCORE.write_scores()
                Snake.increase_speed(True, SCORE.what_is_score())
                Food.move_food()
                Snake.add_snake(1)
                if Snake.special_tally():
                    Food.special_food_available()
                    start = Food.food_time_start()


            if foods == 1:
                SCORE.add_score(8)
                SCORE.write_scores()
                Snake.increase_speed(True, SCORE.what_is_score())
                Snake.add_snake(8)
                if head.distance(food[1].xcor(), food[1].ycor()) <= SNAKES.MOVE_DISTANCE:
                    Food.special_food_unavailable()
        Food.food_time_end()
        if Food.food_time_end() - start >= 5:
            Food.special_food_unavailable()


def write_game_over():
    PEN.hideturtle()
    PEN.penup()
    PEN.right(180)
    PEN.forward(1400)
    time.sleep(.02)
    PEN.color('deep pink')
    PEN.write(f'Your Score Is: {SCORE.score}', font=style, align='center')
    PEN.forward(400)
    PEN.right(180)
    PEN.write(f'---- GAME OVER ----', font=game_over, align='center')


def is_game_over():
    if game_is_over():
        # SCORE.save_high_score()
        write_game_over()
        time.sleep(1)
        game_reset()


def game_is_over():
    global going
    for segment in range(1, len(snake)):
        seg = snake[segment]
        if head.distance(seg.xcor(), seg.ycor()) < SNAKES.MOVE_DISTANCE*.999:
            if seg.distance(head.xcor(), head.ycor()) < SNAKES.MOVE_DISTANCE*.999 and seg.pos() != seg.home():
                SCORE.reset()
                SCORE.clear()
                return True
        if rules.lower() == 'b':
            if boundaries():
                return True
        else:
            no_boundaries()


def game_reset():
    global head
    PEN.clear()
    SCORE.reset_score()
    SCORE.write_scores()
    Snake.reset_snake()
    head = Snake.head
    SCORE.score = 0


def game_go():
    SCORE.write_scores()
    while going:
        Snake.move()
        screen.update()
        # print(f'SNAKE.SPEED is: {Snake.speed}')
        time.sleep(Snake.speed)
        compare_food_coordinates()
        is_game_over()


game_go()
screen.exitonclick()
