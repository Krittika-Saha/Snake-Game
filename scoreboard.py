from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self, score):
    super().__init__()
    self.score = 0
    self.color('white')
    self.hideturtle()
    self.up()
    self.goto(-100, 270)
    self.write(f"Score: {self.score}", align='center', font=("Helvetica", 12, "bold"))
    self.write_high_score()
  def increase_score(self):
    self.goto(-100, 270)
    self.clear()
    self.score += 1
    self.write(f"Score: {self.score}", align='center', font=("Helvetica", 12, "bold"))

  def game_over(self):
    self.goto(0, 0)
    self.write("Game Over", align='center', font=("Helvetica", 12, "bold"))

  def write_high_score(self):
    self.add_high_score()
    self.goto(100, 270)
    self.write(f"High score: {self.high_score}", align='center',font=("Helvetica", 12, "bold"))

  def add_high_score(self):
    self.file = open('high_score.txt', 'r+')
    all_scores = []
    for score in self.file:
      score_int = int(score[:-1])
      all_scores.append(score_int)
    all_scores.append(self.score)
    self.high_score = max(all_scores)
    
  def add_score_to_file(self):
    high_score_str = f"{self.high_score}\n"
    if high_score_str not in self.file:
      self.file.write(high_score_str)
      self.file.close()
    else:
      self.file.close()
    self.file.close()