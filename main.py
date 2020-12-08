from turtle import Screen, Turtle
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Classic snake game')
screen.tracer(0)

snake = Snake('square', 3, 'white')

game_is_on = True

while game_is_on:
  sleep(0.1)
  screen.update()
  
  snake.move()



screen.exitonclick()