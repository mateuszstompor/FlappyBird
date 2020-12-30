from typing import Optional, List
from abc import ABC, abstractmethod
from flappy.ui.view.general import View
from flappy.ui.interaction.general import InteractionProcessor


class ViewController(ABC):
    @abstractmethod
    def view(self) -> Optional[View]:
        pass

    @abstractmethod
    def interaction_processors(self) -> List[InteractionProcessor]:
        pass

    def received_focus(self):
        pass

    def view_redrawn(self):
        pass
