import pygame

from flappy.ui.presenter import Presenter
from flappy.ui.controller.landing import LandingViewController

pygame.init()

screen = pygame.display.set_mode([285, 500])
presenter = Presenter(screen)
presenter.push(LandingViewController(presenter))
presenter.present()

pygame.quit()
