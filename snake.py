
class Snake():

 
  def __init__(self, shape, length, color):

     
    from turtle import Screen, Turtle

    self.shape = shape
    self.length = length
    self.color = color

    self.segments = []
  
    x = 0
    for i in range(length):
      new_segment = Turtle(shape)
      new_segment.up()
      new_segment.color(color)
      new_segment.goto(x=x, y=0)
      self.segments.append(new_segment)
      x -= 20

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num-1].xcor()
      new_y = self.segments[seg_num-1].ycor()
      self.segments[seg_num].goto(new_x, new_y)

    self.segments[0].fd(20)



