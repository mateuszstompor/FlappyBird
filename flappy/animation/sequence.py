from math import floor
from collections import namedtuple
from flappy.animation.stopwatch import StopWatch

Keyframe = namedtuple('Keyframe', ['image', 'length'])


class Animation:
    def __init__(self, keyframes, repeat=False):
        self.keyframes = keyframes
        self.repeat = repeat
        self.timer = StopWatch()

    def rewind(self):
        self.timer.reset()

    def play(self):
        self.timer.start()

    def is_playing(self):
        return self.timer.is_measuring()

    def resume(self):
        self.timer.resume()

    def pause(self):
        self.timer.pause()

    def cursor(self):
        elapsed = self.timer.elapsed_time()
        if self.repeat:
            animation_length = self.animation_length()
            cycles = floor(elapsed / animation_length)
            elapsed = elapsed - cycles * animation_length
        return elapsed

    def image(self):
        elapsed = self.cursor()
        for frame in self.keyframes:
            begin = 0
            if begin <= elapsed < begin + frame.length:
                return frame.image
            begin += frame.length
        return self.keyframes[-1].image

    def animation_length(self):
        return sum([k.length for k in self.keyframes])
