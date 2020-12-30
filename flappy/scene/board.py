from flappy.scene.bird import Bird
from typing import List, NamedTuple
from flappy.scene.obstacle import Obstacle


Board = NamedTuple('Board', [('bird', Bird), ('obstacles', List[Obstacle])])
