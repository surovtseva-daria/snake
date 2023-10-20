import random

import stddraw
from field import size


class Apple:
    def __init__(self):
        self.location = (0, 0)

    def set_random_not(self, not_coord):
        n = 0
        while n == 0:
            x = random.randint(1, size - 1)
            y = random.randint(1, size - 1)
            if (x, y) not in not_coord:
                n = 1
        self.location = (x, y)

    def draw(self):
        x, y = self.location
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(x+0.5, y+0.5, 0.5)
