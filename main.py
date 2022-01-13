from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
is_game_on = True

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #is_game_on = False
        scoreboard.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            #is_game_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
