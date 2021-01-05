import pytest

from flappy.core.choice import WheelChoice


@pytest.fixture
def collection():
    return WheelChoice([1, 2, 3])


@pytest.fixture
def next_item_mapping():
    return {
        1: 2,
        2: 3,
        3: 1
    }


def test_item(collection):
    assert collection.item() in [1, 2, 3]


class TestNextItem:
    def test_returned_value(self, collection, next_item_mapping):
        current = collection.item()
        assert collection.next_item() == next_item_mapping[current]

    def test_iteration(self, collection, next_item_mapping):
        current = collection.item()
        collection.next_item()
        assert collection.item() == next_item_mapping[current]
