from .smoothing_interface import SmoothingInterface
from math import pow, sin


class LinearSmoothing(SmoothingInterface):
    """
    Linear smoothing, returns the input time directly.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        return seconds_time


class EaseOutQuadSmoothing(SmoothingInterface):
    """
    Quadratic ease-out smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        return 1 - (1 - seconds_time) * (1 - seconds_time)


class QuadraticSmoothing(SmoothingInterface):
    """
    Quadratic smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        if seconds_time <= 0.5:
            return 2 * seconds_time * seconds_time
        seconds_time -= 0.5
        return 2 * seconds_time * (1 - seconds_time) + 0.5


class ParametricSmoothing(SmoothingInterface):
    """
    Parametric smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        square = seconds_time * seconds_time
        return square / (2.0 * (square - seconds_time) + 1.0)


class EaseOutQuintSmoothing(SmoothingInterface):
    """
    Quintic ease-out smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        return 1 - pow(1 - seconds_time, 5)


class EaseOutCubicSmoothing(SmoothingInterface):
    """
    Cubic ease-out smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        return 1 - pow(1 - seconds_time, 3)


class EaseOutBackSmoothing(SmoothingInterface):
    """
    Back ease-out smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        c1 = 1.70158
        c3 = c1 + 1
        return 1 + c3 * pow(seconds_time - 1, 3) + c1 * pow(seconds_time - 1, 2)


class EaseInOutElasticSmoothing(SmoothingInterface):
    """
    Elastic ease-in-out smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        c5 = (2 * 3.14159) / 4.5
        if seconds_time == 0:
            return 0
        if seconds_time == 1:
            return 1
        if seconds_time < 0.5:
            return -(pow(2, 20 * seconds_time - 10) * sin((20 * seconds_time - 11.125) * c5)) / 2
        return (pow(2, -20 * seconds_time + 10) * sin((20 * seconds_time - 11.125) * c5)) / 2 + 1


class EaseOutElasticSmoothing(SmoothingInterface):
    """
    Elastic ease-out smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        c4 = (2 * 3.14159) / 3
        if seconds_time == 0:
            return 0
        if seconds_time == 1:
            return 1
        return pow(2, -10 * seconds_time) * sin((seconds_time * 10 - 0.75) * c4) + 1


class EaseOutExpoSmoothing(SmoothingInterface):
    """
    Exponential ease-out smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        return 1 - pow(2, -10 * seconds_time) if seconds_time < 1 else 1


class EaseOutSuperFastSmoothing(SmoothingInterface):
    """
    Super fast ease-out smoothing.
    """
    @staticmethod
    def smooth_in_animation(seconds_time: float) -> float:
        if seconds_time < 0.1:
            return 5 * seconds_time
        else:
            return 1 - pow(2, -10 * (seconds_time - 0.1) / 0.9) * 0.5

