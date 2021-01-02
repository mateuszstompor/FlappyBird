from typing import Optional

import pygame

from flappy.core.stack import Stack
from flappy.ui.system.drawer import ViewDrawer
from flappy.ui.controller.general import ViewController


class Presenter:
    def __init__(self, drawer: ViewDrawer):
        self.__drawer = drawer
        self.__controllers = Stack()

    def push(self, controller: ViewController):
        self.__controllers.push(controller)

    def pop(self):
        self.__controllers.pop()

    def pop_all(self):
        self.__controllers.clear()

    def present(self):
        last_controller: Optional[ViewController] = None
        while self.__controllers:
            controller = self.__controllers.top()
            if last_controller != controller:
                if last_controller is not None:
                    last_controller.lost_focus()
                controller.received_focus()
                last_controller = controller
            events = pygame.event.get()
            for processor in controller.interaction_processors():
                if processor.responds(events) and not processor.allows_other():
                    break
            self.__redraw_hierarchy()

    def __redraw_hierarchy(self):
        for controller in self.__controllers.from_bottom():
            self.__drawer.draw_recursively(controller.view())
            controller.view_redrawn()
        pygame.display.flip()
