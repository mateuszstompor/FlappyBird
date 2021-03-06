from typing import Optional, List
from abc import ABC, abstractmethod
from flappy.ui.view.general import View
from flappy.ui.interaction.general import InteractionProcessor


class ViewController(ABC):
    """
    Interface of all controllers that can be pushed onto
    the navigation stack. Each controller has an associated view
    that starts to be rendered once the controller obtains focus.
    A controller can handle inputs from the user by providing
    appropriate handler in the list of interaction processors
    """
    @abstractmethod
    def view(self) -> Optional[View]:
        pass

    @abstractmethod
    def interaction_processors(self) -> List[InteractionProcessor]:
        pass

    def received_focus(self):
        pass

    def lost_focus(self):
        pass

    def view_redrawn(self):
        pass
