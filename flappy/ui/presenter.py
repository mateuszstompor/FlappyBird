import pygame

from typing import List
from flappy.ui.controller.general import ViewController


class Presenter:
    def __init__(self, surface):
        self.__surface = surface  # type: pygame.Surface
        self.__controllers = []  # type: List[ViewController]

    def push(self, controller: ViewController):
        self.__controllers.append(controller)

    def pop(self):
        self.__controllers.pop(len(self.__controllers) - 1)

    def pop_all(self):
        self.__controllers = []

    def present(self):
        while self.__controllers:
            controller = self.__controllers[-1]
            controller.view().draw(self.__surface)
            controller.received_focus()
            while self.__controllers and controller == self.__controllers[-1]:
                events = pygame.event.get()
                for processor in controller.interaction_processors():
                    processor.process(events)
                controller.view().draw(self.__surface)
