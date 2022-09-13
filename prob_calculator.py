import copy
import random
# Consider using the modules imported above.

class Hat:
  # *args allows you to pass the desired number of arguments to the function. The only difference from args is that it uses keywords and returns the values in the form of a dictionary.
  def __init__(self, **kwargs):
    self.contents = sum([[key] * value for key, value in kwargs.items()], [])

  def draw(self, balls):
    if balls > len(self.contents):
      return self.contents
    else:
      sample = random.sample(self.contents, balls)
      for x in sample:
        self.contents.remove(x)
      return sample
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  if num_balls_drawn > len(hat.contents):
    return 1
  else:
    num_events = 0
    for i in range(num_experiments):
      sample = random.sample(hat.contents, num_balls_drawn)
      actual_events = {ball: sample.count(ball) for ball in set(sample)}
      
      lst = []
      for key, value in expected_balls.items():
        if key in actual_events and actual_events[key] >= value:
          lst.append(True)
        else:
          lst.append(False)
          
      if False in lst:
        continue
      else:
        num_events += 1
        
    return num_events/num_experiments