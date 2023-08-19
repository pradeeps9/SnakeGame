from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from playagain import Playagain
import time

my_screen = Screen()


def screen_setup():

    my_screen.setup(width=600, height=600)
    my_screen.title("Snake Game")
    my_screen.bgcolor("black")
    my_screen.tracer(0)


def snake_moves():

    snk = Snake()
    my_screen.listen()
    my_screen.onkey(snk.up, "Up")
    my_screen.onkey(snk.down, "Down")
    my_screen.onkey(snk.left, "Left")
    my_screen.onkey(snk.right, "Right")
    my_screen.onkey(playagain.pause, "space")

    return snk


def play_game():
    my_screen.clearscreen()
    start_game()


def exit_game():
    my_screen.bye()


playagain = Playagain()


def game_over_screen():

    playagain.create_option()

    my_screen.onkey(fun=exit_game, key="e")
    my_screen.onkey(fun=play_game, key="p")


def start_game():
    is_game_on = True

    screen_setup()
    snake = snake_moves()
    food = Food()
    scoreboard = Scoreboard()

    while is_game_on:
        my_screen.update()
        time.sleep(0.1)

        snake.move()

        # Eat food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extent()

        # Detect collision with walls
        if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
            is_game_on = False
            playagain.game_over()
            scoreboard.reset_score()
            snake.reset_snake()

        # Detect collision with its own tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                playagain.game_over()
                scoreboard.reset_score()
                snake.reset_snake()



start_game()

my_screen.exitonclick()
