# Pygame-Animation
This package provides a framework for managing animations using various smoothing techniques. The AnimationManager class is designed to handle the setup and progression of animations, allowing for smooth transitions and customizable easing methods.

# Features
## 1. Customizable Smoothing: 
Use different smoothing methods to control the animation's easing.
## 2. Flexible Activation: 
Easily manage the activation and deactivation of animations.
## 3. Abstract Methods for Custom Animations: 
Implement your own animations by extending the AnimationManager class.

# Installation
Ensure that the module and its dependencies are included in your project. No additional installation steps are required.
```bash
pip install pygame-animations
```

# Usage
## Importing the Classes
```python
from smoothing_methods import EaseOutSuperFastSmoothing, SmoothingInterface
from smooth_animation import SmoothAnimation
from target_manager import TargetManager
from animation_manager import AnimationManager"
```
## Creating a Custom Animation Manager
To create a custom animation, extend the AnimationManager class and implement the abstract methods animate, activated_animation_setup, and deactivated_animation_setup.

```python
class MyCustomAnimationManager(AnimationManager):
    """
    A custom animation manager for manipulating the position of a surface.

    Args:
        surface: The surface object to be animated.
    """
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        
    def animate(self):
        """Animate the surface's position."""
        self.surface.set_position(self.current_value)

    def activated_animation_setup(self):
        """
        Set up the animation for the activated state.

        Initial position of the surface: 10
        Target position of the surface: 20
        """
        self.set_target(current_value=10, target_value=20)

    def deactivated_animation_setup(self):
        """
        Set up the animation for the deactivated state.

        Initial position of the surface: 20
        Target position of the surface: 10
        """
        self.set_target(current_value=20, target_value=10)

```
# Usage example
```python
animation_manager = MyCustomAnimationManager(activated=False, percentage_per_iteration=0.05)
animation_manager.check_for_animation(activated=True)
```
# Class Descriptions
## AnimationManager
The AnimationManager class is an abstract base class for managing animations. It handles the setup and progression of animations using a SmoothAnimation instance.

## Initialization
```python
AnimationManager(activated: bool = False, percentage_per_iteration: float = 0.03, smoothing_method: SmoothingInterface = EaseOutSuperFastSmoothing())
```
## activated: 
Initial activation state of the animation (default: False).
## percentage_per_iteration: 
The percentage change per iteration for the animation (default: 0.03).
## smoothing_method: 
The smoothing method to use for the animation (default: EaseOutSuperFastSmoothing).
# Smoothing Methods
This module also provides various smoothing methods to control the easing of animations. Each smoothing method implements the SmoothingInterface and provides a static method smooth_in_animation to calculate the smoothed value based on the elapsed time.

## LinearSmoothing
### Description: 
Linear smoothing, returns the input time directly.
## EaseOutQuadSmoothing
### Description: 
Quadratic ease-out smoothing.
## QuadraticSmoothing
### Description: 
Quadratic smoothing with different behavior based on time.
## ParametricSmoothing
### Description: 
Parametric smoothing using a specific parametric formula.
## EaseOutQuintSmoothing
### Description: 
Quintic ease-out smoothing.
## EaseOutCubicSmoothing
### Description: 
Cubic ease-out smoothing.
## EaseOutBackSmoothing
### Description: 
Back ease-out smoothing with overshoot.
## EaseInOutElasticSmoothing
### Description: 
Elastic ease-in-out smoothing with a bounce effect.
## EaseOutElasticSmoothing
### Description: 
Elastic ease-out smoothing with a bounce effect.
## EaseOutExpoSmoothing
### Description: 
Exponential ease-out smoothing.
## EaseOutSuperFastSmoothing
### Description: 
Super fast ease-out smoothing, starts quickly then slows down exponentially.

# Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions for improvements or new features.

# License
This project is licensed under the MIT License.