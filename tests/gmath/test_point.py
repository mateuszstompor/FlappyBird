from flappy.gmath.point import Point


def test_addition():
    p1, p2 = Point(1, 1), Point(2, 2)
    result = p1 + p2
    assert result.x == result.y == 3


def test_difference():
    p1, p2 = Point(1, 1), Point(2, 2)
    result = p1 - p2
    assert result.x == result.y == -1


def test_offset():
    p = Point(1, 1)
    result = p.offset(4, 4)
    assert 5 == result.x == result.y


class TestEquality:
    class TestSameType:
        def test_equal(self):
            assert Point(0, 0) == Point(0, 0)

        def test_not_equal(self):
            assert Point(0, 0) != Point(10, 1)

    def test_different_types(self):
        assert Point(0, 0) != 0
