from .smoothing_methods import EaseOutCubicSmoothing, SmoothingInterface
from .target_manager import TargetManager


class SmoothAnimation:
    """
    Manages smooth animations using a target manager and smoothing method.
    """
    __reset_animation: bool = False
    __finished_animation: bool = False

    def __init__(self, target_manager: TargetManager, speed_per_frame: float,
                 smoothing_method: SmoothingInterface = EaseOutCubicSmoothing()):
        """
        Initializes the SmoothAnimation.

        Args:
            target_manager (TargetManager): The target manager instance.
            speed_per_frame (float): The speed of the animation per frame.
            smoothing_method (SmoothingInterface): The smoothing method to be used for the animation.
        """
        self.__animation = _Animation(ms_interval_per_iteration=speed_per_frame, smoothing_method=smoothing_method)
        self.__target_manager = target_manager

    def reset(self) -> None:
        """
        Resets the animation to its initial state.
        """
        self.__reset_animation = False
        self.__finished_animation = False
        self.__animation.reset()

    def __smooth_out_animation(self) -> None:
        """
        Ensures the animation is reset if it hasn't been already.
        """
        if not self.__reset_animation:
            self.__animation.reset()
        self.__reset_animation = True

    def get_current_value(self) -> float:
        """
        Gets the current value of the animation.

        Returns:
            float: The current animated value.
        """
        add_value = self.__get_add_value
        value = self.__target_manager.current_value + add_value
        if self.__target_manager.check_if_equal_target_value(value=value):
            self.__finished_animation = True
        return value

    @property
    def __get_add_value(self) -> float:
        """
        Calculates the additional value to be added to the current value.

        Returns:
            float: The additional value.
        """
        return self.__target_manager.target_value_range * self.__animation.get_current_percentage()

    @property
    def finished_animation(self) -> bool:
        """
        Checks if the animation is finished.

        Returns:
            bool: True if the animation is finished, False otherwise.
        """
        return self.__finished_animation

    def change_interval(self, ms_interval: float) -> None:
        """
        Changes the interval between frames for the animation.

        Args:
            ms_interval (float): The new interval in milliseconds.
        """
        self.__animation.change_interval(ms_interval=ms_interval)


class _Animation:
    """
    Handles the core animation timing and smoothing logic.
    """
    __MAX_TIME: float = 1.01
    __current_seconds: float = 0

    def __init__(self, ms_interval_per_iteration: float, smoothing_method: SmoothingInterface):
        """
        Initializes the _Animation.

        Args:
            ms_interval_per_iteration (float): The interval per iteration in milliseconds.
            smoothing_method (SmoothingInterface): The smoothing method to be used for the animation.
        """
        self.__ms_interval_per_iteration = ms_interval_per_iteration
        self.__smoothing_method = smoothing_method

    def run(self) -> None:
        """
        Runs the animation by updating the current time and applying the smoothing method.
        """
        if self.__finished():
            return
        self.__smoothing_method.smooth_in_animation(seconds_time=self.__current_seconds)
        self.__current_seconds += self.__ms_interval_per_iteration

    def get_current_percentage(self) -> float:
        """
        Gets the current percentage of the animation's completion.

        Returns:
            float: The current completion percentage.
        """
        if self.__finished():
            return 1
        percentage = self.__smoothing_method.smooth_in_animation(seconds_time=self.__current_seconds)
        self.__current_seconds += self.__ms_interval_per_iteration
        return percentage

    def __finished(self) -> bool:
        """
        Checks if the animation is finished.

        Returns:
            bool: True if the animation is finished, False otherwise.
        """
        return self.__current_seconds > self.__MAX_TIME

    def reset(self) -> None:
        """
        Resets the animation to the initial state.
        """
        self.__current_seconds = 0

    def change_interval(self, ms_interval: float) -> None:
        """
        Changes the interval between frames for the animation.

        Args:
            ms_interval (float): The new interval in milliseconds.
        """
        self.__ms_interval_per_iteration = ms_interval


