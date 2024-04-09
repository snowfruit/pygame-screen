"""Docstring."""

from pygame_screen.screen import Screen

# Naming is done by matching css naming conventions.
# Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit


class ScreenCenterFixedSize(Screen):
    """
    Based on Screen-class. Do not resize canvas-surface.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
    """

    def update(self) -> None:
        # FixedCenter-fit only needs to update position.
        self.update_position()
