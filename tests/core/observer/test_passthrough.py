import pytest

from unittest.mock import Mock

from flappy.core.observer.passthrough import PassthroughSubject


@pytest.fixture
def uut():
    return PassthroughSubject()


class TestAttach:
    def test_first_call(self, uut):
        observer = Mock()
        uut.attach(observer)
        assert observer in uut.observers()

    def test_duplicates(self, uut):
        observer = Mock()
        uut.attach(observer)
        uut.attach(observer)
        assert isinstance(uut.observers(), set)


class TestDetach:
    def test_observer_present(self, uut):
        observer = Mock()
        uut.attach(observer)
        uut.detach(observer)
        assert observer not in uut.observers()

    def test_observer_absent(self, uut):
        observer = Mock()
        uut.detach(observer)
        assert observer not in uut.observers()


class TestNotify:
    def test_no_observers(self, uut):
        uut.notify(None)

    class TestObserversPresent:
        def test_single(self, uut):
            observer, event = Mock(), Mock()
            uut.attach(observer)
            uut.notify(event)
            observer.update.assert_called_with(uut, event)

        def test_multiple(self, uut):
            observer_a, observer_b, event = Mock(), Mock(), Mock()
            uut.attach(observer_a)
            uut.attach(observer_b)
            uut.notify(event)
            for observer in (observer_a, observer_b):
                observer.update.assert_called_with(uut, event)
