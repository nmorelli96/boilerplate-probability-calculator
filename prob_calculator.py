import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **hat_balls):
        self.contents = []
        for key, value in hat_balls.items():
            n = value
            while n > 0:
                self.contents.append(key)
                n -= 1
    def __str__(self):
        return str(self.contents)
    def draw(self, balls_drawn_qty):
        balls_drawn = []
        n = balls_drawn_qty
        if n > len(self.contents):
            return self.contents
        while n > 0:
            pick = random.choice(self.contents)
            balls_drawn.append(pick)
            self.contents.remove(pick)
            n -= 1
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n = num_experiments
    m = 0   #times we get the expected goals
    while n > 0:
        hat_copy = copy.deepcopy(hat) #creates a new independent copy of hat before each experiment
        draw = hat_copy.draw(num_balls_drawn)
        t = 0  # times we get a single expected ball (not the whole group)
        for ball, count in expected_balls.items():
            if draw.count(ball) >= count:
                t += 1
        if t >= len(expected_balls):
            m += 1
        n -= 1
    return m/num_experiments
