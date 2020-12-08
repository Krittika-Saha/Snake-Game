from turtle import Screen, Turtle
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Classic snake game')
screen.tracer(0)


segments = []
x = 0
for i in range(3):
  new_segment = Turtle('square')
  new_segment.up()
  new_segment.color('white')
  new_segment.goto(x=x, y=0)
  segments.append(new_segment)
  x -= 20


game_is_on = True

while game_is_on:
  sleep(0.1)
  screen.update()
  
  for seg_num in range(len(segments) - 1, 0, -1):
    new_x = segments[seg_num-1].xcor()
    new_y = segments[seg_num-1].ycor()
    segments[seg_num].goto(new_x, new_y)

  segments[0].fd(20)




screen.exitonclick()