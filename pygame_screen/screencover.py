"""Docstring."""

from pygame_screen.fit import objectfit
from pygame_screen.screen import Screen

# Naming is done by matching css naming conventions.
# Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit


class ScreenCover(Screen):
    """
    Based on Screen-class. Applies a cover-style to canvas-surface.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit#cover
    """

    def update_scale(self) -> None:
        self.geometry.scale = objectfit.resize_cover(
            self.screen.get_size(),
            self.canvas.get_size(),
            self.settings.use_integer_scaling,
            self.settings.clamp_size,
        )
