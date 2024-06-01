from .smoothing_methods import EaseOutSuperFastSmoothing, SmoothingInterface
from .smooth_animation import SmoothAnimation
from .target_manager import TargetManager
from abc import ABC, abstractmethod


class AnimationManager(ABC):
    def __init__(self, activated: bool = False, percentage_per_iteration: float = 0.03, smoothing_method:
                 SmoothingInterface = EaseOutSuperFastSmoothing()):
        """
        Initializes the AnimationManager.

        Args:
            activated (bool): Initial activation state of the animation. Defaults to False.
            percentage_per_iteration (float): The percentage change per iteration for the animation. Defaults to 0.03.
        """
        self.__target_manager = TargetManager()
        self.__animation_manager = SmoothAnimation(
            target_manager=self.__target_manager,
            speed_per_frame=percentage_per_iteration,
            smoothing_method=smoothing_method
        )
        self.__start_manager = _AnimationStartManager()
        self.__activated = activated

    def check_for_animation(self, activated: bool) -> None:
        """
        Checks whether the animation should be triggered based on the activation status.

        Args:
            activated (bool): The current activation status.
        """
        if self.__correct_conditions(activated=activated):
            self.animate()

    def __correct_conditions(self, activated: bool) -> bool:
        """
        Determines if the conditions are correct to start the animation.

        Args:
            activated (bool): The current activation status.

        Returns:
            bool: True if conditions are met to start the animation, False otherwise.
        """
        if self.__animation_manager.finished_animation:
            self.__start_manager.start_animation = False
        self.check_if_init_animate(activated=activated)
        if not self.__start_manager.start_animation:
            return False
        return True

    @abstractmethod
    def animate(self) -> None:
        """
        Abstract method to perform the animation. Must be implemented by subclasses.
        """
        pass

    @property
    def current_value(self) -> float:
        """
        Gets the current value of the animation.

        Returns:
            float: The current value of the animation.
        """
        return self.__animation_manager.get_current_value()

    def check_if_init_animate(self, activated: bool) -> None:
        """
        Checks if the animation should be initialized.

        Args:
            activated (bool): The current activation status.
        """
        if self.__activated != activated:
            self.__setup_animation(activated=activated)

    def __setup_animation(self, activated: bool) -> None:
        """
        Sets up the animation based on the activation status.

        Args:
            activated (bool): The current activation status.
        """
        self.__animation_manager.reset()
        if activated:
            self.activated_animation_setup()
        else:
            self.deactivated_animation_setup()
        self.__activated = activated
        self.__start_manager.start_animation = True

    @abstractmethod
    def activated_animation_setup(self) -> None:
        """
        Abstract method to set up the animation when activated. Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def deactivated_animation_setup(self) -> None:
        """
        Abstract method to set up the animation when deactivated. Must be implemented by subclasses.
        """
        pass

    def set_target(self, current_value: int, target_value: int) -> None:
        """
        Set up the target manager with the current and target values.

        Args:
            current_value (int): The current value before the animation starts.
            target_value (int): The desired target value to reach after the animation.
        """
        self.__target_manager.setup(current_value=current_value, target_value=target_value)


class _AnimationStartManager:
    start_animation: bool = False
