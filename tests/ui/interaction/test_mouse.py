from unittest.mock import Mock, patch

import pygame
import pytest

from flappy.gmath.point import Point
from flappy.ui.interaction.mouse import TapHandler
from flappy.ui.view.blueprint import BlueprintView


def test_allow_others():
    uut = TapHandler(BlueprintView(None, Point(0, 0)), None)
    assert not uut.allows_other()


class TestResponds:
    class TestNoMatch:
        def test_no_events(self):
            uut = TapHandler(BlueprintView(None, Point(0, 0)), None)
            assert not uut.responds([])

        def test_no_matching_event(self):
            uut = TapHandler(BlueprintView(None, Point(0, 0)), None)
            assert not uut.responds([Mock(type=pygame.KEYUP)])

    class TestMatch:
        def test_delegate_call(self):
            with patch('flappy.ui.interaction.mouse.pygame.mouse.get_pos', Mock(return_value=(0.5, 0.5))):
                delegate = Mock()
                view = Mock(compose=Mock(return_value=Mock(get_rect=Mock(return_value=(0, 0, 1, 1)))),
                            offset=Mock(return_value=Point(0, 0)),
                            parent_view=Mock(return_value=None))
                uut = TapHandler(view, delegate)
                uut.responds([Mock(type=pygame.MOUSEBUTTONDOWN)])
                delegate.tapped.assert_called_once()

        def test_responds(self):
            with patch('flappy.ui.interaction.mouse.pygame.mouse.get_pos', Mock(return_value=(0.5, 0.5))):
                view = Mock(compose=Mock(return_value=Mock(get_rect=Mock(return_value=(0, 0, 1, 1)))),
                            offset=Mock(return_value=Point(0, 0)),
                            parent_view=Mock(return_value=None))
                uut = TapHandler(view, None)
                assert uut.responds([Mock(type=pygame.MOUSEBUTTONDOWN)])
