class TargetManager:
    """
    Manages the target values for animations, including the current value, target value, and the range between them.
    """

    __target_value_range: float = 0
    __current_value: float = 0
    __target_value: float = 0

    def setup(self, current_value: float, target_value: float) -> None:
        """
        Sets up the target manager with the current value and the target value.
        This should only be called once per change.

        Args:
            current_value (float): The current value before the animation starts.
            target_value (float): The desired target value to reach after the animation.
        """
        self.__target_value_range = target_value - current_value
        self.__current_value = current_value
        self.__target_value = target_value

    @property
    def target_value_range(self) -> float:
        """
        The range between the current value and the target value.

        Returns:
            float: The difference between the target value and the current value.
        """
        return self.__target_value_range

    @property
    def current_value(self) -> float:
        """
        The current value of the animation.

        Returns:
            float: The current value.
        """
        return self.__current_value

    @property
    def target_value(self) -> float:
        """
        The target value for the animation.

        Returns:
            float: The target value.
        """
        return self.__target_value

    def check_if_equal_target_value(self, value: float) -> bool:
        """
        Checks if the provided value is equal to the target value.

        Args:
            value (float): The value to check against the target value.

        Returns:
            bool: True if the value is equal to the target value, False otherwise.
        """
        return value == self.__target_value
