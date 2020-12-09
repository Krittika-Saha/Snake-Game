from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Classic snake game')
screen.tracer(0)

snake = Snake('square', 3, 'white')
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
  sleep(0.1)
  screen.update()
  
  snake.move()

  #Detect collision with food

  if snake.head.distance(food) <= 15:
    food.refresh()
  


screen.exitonclick()