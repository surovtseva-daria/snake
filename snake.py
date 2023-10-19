import stddraw
from color import Color

from field import size


class Snake:
    def __init__(self):
        self.telo = [(size // 2, size // 2)]
        self.glaz = 'в'
        # 'в'-вперед, 'н'-назад 'л'-лево 'п'-право

    def move(self):
        self.grow()
        self.telo.pop(-1)

    def golova(self):
        return self.telo[0]

    def draw(self):
        for x, y in self.telo:
            stddraw.setPenColor(Color( 0, 100, 0))
            stddraw.filledSquare(x+0.5, y+0.5, 0.5)

    def left(self):
        if (self.glaz != 'п'):
            self.glaz = 'л'

    def right(self):
        if (self.glaz != 'л'):
            self.glaz = 'п'

    def down(self):
        if (self.glaz != 'в'):
            self.glaz = 'н'

    def up(self):
        if (self.glaz != 'н'):
            self.glaz = 'в'

    def grow(self):
        x, y = self.next_golova()
        self.telo.insert(0, (x, y))

    def next_golova(self):
        x, y = self.golova()
        if self.glaz == 'в':
            y += 1
        if self.glaz == 'н':
            y -= 1
        if self.glaz == 'п':
            x += 1
        if self.glaz == 'л':
            x -= 1
        return x, y

    def eat(self, location):
        if location == self.next_golova():
            self.grow()
            return True
        else:
            return False

