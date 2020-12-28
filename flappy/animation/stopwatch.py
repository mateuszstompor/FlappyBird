from time import time


class InvalidInvocation(Exception):
    pass


class StopWatch:
    def __init__(self):
        self.__elapsed = 0.0
        self.__last_start = None
        self.__paused = False

    def elapsed_time(self):
        if self.__paused:
            return self.__elapsed
        elif self.__last_start is None:
            return self.__elapsed
        return time() - self.__last_start + self.__elapsed

    def pause(self):
        self.__elapsed = time() - self.__last_start
        self.__paused = True

    def is_measuring(self):
        return self.__last_start is not None

    def resume(self):
        self.__paused = False
        self.__last_start = time()

    def is_paused(self):
        return self.__paused

    def reset(self):
        self.stop()
        self.start()

    def stop(self):
        self.__elapsed = 0.0
        self.__last_start = None
        self.__paused = False

    def start(self):
        if self.__last_start is not None:
            raise InvalidInvocation('Timer already started')
        self.__last_start = time()
