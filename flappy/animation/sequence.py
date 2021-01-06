from math import floor
from typing import NamedTuple, Any, List
from flappy.animation.stopwatch import StopWatch


Keyframe = NamedTuple('Keyframe', [('data', Any), ('length', float)])


class SequenceAnimation:
    """
    The class provides a set of methods to retrieve a keyframe
    from the list based on elapsed time. Animation which is built
    by that sequence can be paused, resumed and rewound once it
    finishes
    """
    def __init__(self, keyframes: List[Keyframe], repeat=False):
        self.keyframes = keyframes
        self.repeat = repeat
        self.__timer = StopWatch()

    def rewind(self):
        self.__timer.reset()

    def play(self):
        self.__timer.start()

    def is_playing(self) -> bool:
        return self.__timer.is_measuring()

    def resume(self):
        self.__timer.resume()

    def pause(self):
        self.__timer.pause()

    def cursor(self) -> float:
        elapsed = self.__timer.elapsed_time()
        if self.repeat:
            animation_length = self.animation_length()
            cycles = floor(elapsed / animation_length)
            elapsed = elapsed - cycles * animation_length
        return elapsed

    def data(self) -> Any:
        elapsed = self.cursor()
        for frame in self.keyframes:
            begin = 0
            if begin <= elapsed < begin + frame.length:
                return frame.data
            begin += frame.length
        return self.keyframes[-1].data

    def animation_length(self) -> float:
        return sum([k.length for k in self.keyframes])
