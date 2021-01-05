from time import sleep

from flappy.animation.stopwatch import StopWatch


def test_pause():
    timer = StopWatch()
    timer.start()
    timer.pause()
    sample = timer.elapsed_time()
    assert sample == timer.elapsed_time()


def test_is_paused():
    timer = StopWatch()
    timer.start()
    timer.pause()
    assert timer.is_paused()


class TestElapsedTime:
    def test_not_started_timer(self):
        timer = StopWatch()
        assert timer.elapsed_time() == 0

    def test_started_time(self):
        timer = StopWatch()
        timer.start()
        sleep(0.1)
        assert timer.elapsed_time() >= 0.1


class TestStop:
    def test_first_call(self):
        timer = StopWatch()
        timer.start()
        sleep(0.1)
        timer.stop()
        elapsed_time = timer.elapsed_time()
        sleep(0.1)
        assert elapsed_time == timer.elapsed_time()


class TestReset:
    def test_stopped(self):
        timer = StopWatch()
        timer.start()
        sleep(0.1)
        timer.stop()
        timer.reset()
        assert timer.elapsed_time() == 0
