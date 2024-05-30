from abc import ABC, abstractmethod


class SmoothingInterface(ABC):
    """
    Interface for smoothing methods used in animations.
    """

    @staticmethod
    @abstractmethod
    def smooth_in_animation(seconds_time: float) -> float:
        """
        Applies smoothing to the animation based on the elapsed time in seconds.

        Args:
            seconds_time (float): The elapsed time in seconds.

        Returns:
            float: The smoothed value based on the elapsed time.
        """
        pass
