from snake import Snake


def test_move():
    s = Snake()
    s.move()
    assert s.telo == [(15, 16)]


def test_move_up():
    s = Snake()
    s.up()
    s.move()
    s.move()
    assert s.telo == [(15, 17)]


def test_move_down():
    s = Snake()
    s.down()
    s.move()
    assert s.telo == [(15, 14)]


def test_move_left():
    s = Snake()
    s.left()
    s.move()
    assert s.telo == [(14, 15)]


def test_move_right():
    s = Snake()
    s.right()
    s.move()
    assert s.telo == [(16, 15)]


def test_move_up_down():
    s = Snake()
    s.up()
    s.move()
    s.down()
    s.move()
    assert s.telo == [(15, 17)]


def test_move_down_up():
    s = Snake()
    s.right()
    s.move()
    s.down()
    s.move()
    s.up()
    s.move()
    assert s.telo == [(16, 13)]

def test_grow():
    s = Snake()
    s.grow()
    assert s.telo == [(15, 16), (15, 15)]



def test_move_right_left():
    s = Snake()
    s.right()
    s.move()
    s.left()
    s.move()
    assert s.telo == [(17, 15)]


def test_move_left_right():
    s = Snake()
    s.left()
    s.move()
    s.right()
    s.move()
    assert s.telo == [(13, 15)]
