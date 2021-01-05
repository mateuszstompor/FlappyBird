from time import time


class StopWatch:
    def __init__(self):
        self.__elapsed = 0.0
        self.__last_start = None
        self.__paused = False

    def elapsed_time(self) -> float:
        if self.__paused:
            return self.__elapsed
        if self.__last_start is None:
            return self.__elapsed
        return time() - self.__last_start + self.__elapsed

    def pause(self):
        self.__elapsed = time() - self.__last_start
        self.__paused = True

    def is_measuring(self) -> bool:
        return self.__last_start is not None

    def resume(self):
        self.__paused = False
        self.__last_start = time()

    def is_paused(self) -> bool:
        return self.__paused

    def reset(self):
        self.__elapsed = 0.0
        self.__last_start = None if (self.__paused or not self.__last_start) else time()

    def stop(self):
        self.__elapsed = 0.0
        self.__last_start = None
        self.__paused = False

    def start(self):
        self.__elapsed = 0.0
        self.__paused = False
        self.__last_start = time()
