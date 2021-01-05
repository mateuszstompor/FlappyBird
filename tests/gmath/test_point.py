from flappy.gmath.point import Point


def test_addition():
    p1, p2 = Point(1, 1), Point(2, 2)
    result = p1 + p2
    assert result.x == result.y == 3
