from scoreboard import ScoreBoard
from turtle import Turtle, Screen
import time
from snake_class import Snake
from class_food import Food



# Create screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("grey")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision with food
    if snake.head.distance(food) < 15:
        food.screen_refresh()
        snake.extend()
        scoreboard.increase_score()


# Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.xcor() > 300 or snake.head.ycor() < -300:
        is_on = False
        scoreboard.game_over()


# Detect collision with tail
for square in snake.squares:
    if square == snake.head:
        pass
    elif snake.head.distance(square) < 10:
        is_on = False
        scoreboard.game_over()



from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.shape("circle")
        self.goto(0, 270)

    def scoreboard_update(self):
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.scoreboard_update()


from turtle import Turtle
import random
STARTING_POSITION = [(0, 0), (-20, 0), (-30, 0)]  # Create the snake body
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_squares(position)


    def add_squares(self, position):
        hanna = Turtle()
        hanna.color("purple")
        hanna.shape("square")
        hanna.penup()
        hanna.goto(position)
        self.squares.append(hanna)

    def extend(self):
        self.add_squares(self.squares[-1].position())

    def move(self):
        for square in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)
        self.head.forward(MOVE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

from turtle import Turtle

import random

class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.screen_refresh()


    def screen_refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)




screen.exitonclick()
