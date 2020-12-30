import pygame

from flappy.core.stack import Stack
from flappy.ui.controller.general import ViewController


class Presenter:
    def __init__(self, surface):
        self.__surface = surface  # type: pygame.Surface
        self.__controllers = Stack()

    def push(self, controller: ViewController):
        self.__controllers.push(controller)

    def pop(self):
        self.__controllers.pop()

    def pop_all(self):
        self.__controllers.clear()

    def present(self):
        while self.__controllers:
            controller = self.__controllers.top()
            self.__redraw_view(controller)
            controller.received_focus()
            while self.__controllers and controller == self.__controllers.top():
                events = pygame.event.get()
                for processor in controller.interaction_processors():
                    processor.process(events)
                self.__redraw_view(controller)

    def __redraw_view(self, controller: ViewController):
        controller.view().draw(self.__surface)
        controller.view_redrawn()
