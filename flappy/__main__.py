import pygame

from flappy.ui.system.presenter import Presenter, ViewDrawer
from flappy.ui.controller.landing import LandingViewController

pygame.init()

screen = pygame.display.set_mode([285, 500])

presenter = Presenter(ViewDrawer(screen))
presenter.push(LandingViewController(presenter))
presenter.present()

pygame.quit()
