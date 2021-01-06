from unittest.mock import Mock

import pygame

from flappy.ui.interaction.keyboard import KeyboardProcessor


def test_allow_others():
    uut = KeyboardProcessor(None)
    assert uut.allows_other()


class TestResponds:
    class TestNoMatch:
        def test_no_events(self):
            uut = KeyboardProcessor(None)
            assert not uut.responds([])

        def test_no_matching_event(self):
            delegate = Mock()
            uut = KeyboardProcessor(delegate)
            assert not uut.responds([Mock(type=pygame.MOUSEBUTTONDOWN)])

    class TestMatch:
        def test_delegate_call(self):
            delegate = Mock()
            uut = KeyboardProcessor(delegate)
            uut.responds([Mock(type=pygame.KEYUP, key=pygame.K_SPACE)])
            delegate.key_released.assert_called_once()

    def test_match(self):
        uut = KeyboardProcessor(None)
        assert uut.responds([Mock(type=pygame.KEYUP, key=pygame.K_SPACE)])
