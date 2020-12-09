from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self, score):
    super().__init__()
    self.score = 0
    self.color('white')
    self.hideturtle()
    self.up()
    self.goto(0, 270)
    self.write(f"Score: {self.score}", align='center', font=("Helvetica", 12, "bold"))

  def increase_score(self):
    self.clear()
    self.score += 1
    self.write(f"Score: {self.score}", align='center', font=("Helvetica", 12, "bold"))



  

  