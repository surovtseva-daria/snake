import stddraw
import field
import snake
import apple


def game_not_over():
    x, y = s.golova()
    if 0 < x < field.size-1 and 0 < y < field.size-1:
        return True
    else:
        return False


field.create()
s = snake.Snake()
a = apple.Apple()
a.set_random_not(s.telo)

while game_not_over():
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'a':
            s.left()
        if key == 's':
            s.down()
        if key == 'w':
            s.up()
        if key == 'd':
            s.right()
    if s.eat(a.location):
        a.set_random_not(s.telo)

    s.move()
    field.create()
    s.draw()
    a.draw()
    stddraw.show(200)


print('Game Over!')
