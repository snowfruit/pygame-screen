"""Please edit this docstring."""

from pygame_screen.screen import Screen

# Naming is done by matching css naming conventions.
# Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit


class ScreenNone(Screen):
    """
    Based on Screen-class. Same as ScreenFixed.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
    """

    def update(self) -> None:
        # Fixed-fit do not need to update scale or position.
        pass
