import pytest

from flappy.core.stack import Stack, EmptyStack


@pytest.fixture
def non_empty_stack():
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')
    return s


def test_clear(non_empty_stack):
    non_empty_stack.clear()
    with pytest.raises(EmptyStack):
        non_empty_stack.top()


def test_top(non_empty_stack):
    assert non_empty_stack.top() == 'c'


class TestPop:
    def test_empty(self):
        with pytest.raises(EmptyStack):
            Stack().pop()

    def test_non_empty(self, non_empty_stack):
        assert non_empty_stack.pop() == 'c'


class TestPush:
    def test_empty(self):
        s = Stack()
        s.push('a')
        assert s.top() == 'a'

    def test_non_empty(self, non_empty_stack):
        non_empty_stack.push('a')
        assert non_empty_stack.top() == 'a'


class TestIterator:
    def test_empty(self):
        assert list(Stack().from_bottom()) == []

    def test_non_empty(self, non_empty_stack):
        assert list(non_empty_stack.from_bottom()) == ['a', 'b', 'c']
