"""Docstring."""

from pygame_screen.fit import objectfit
from pygame_screen.screencontain import ScreenContain

# Naming is done by matching css naming conventions.
# Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit


class ScreenScaleDown(ScreenContain):
    """
    Based on Screen-class. Canvas-surface is 1.0 or smaller in scale.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit#scale-down
    """

    def update_scale(self) -> None:
        # Notice that integer-scaling and clamp and is set to False.
        # ScreenCenter is an better alternativ if change is wanted.
        self.geometry.scale = objectfit.resize_scale_down(
            self.screen.get_size(),
            self.canvas.get_size(),
            False,
            False,
        )

        # ScreenContain use same x and y value for scale.
        # TODO: If integer scaling is used it can be a problem in the future.
        new_scale, _ = self.geometry.scale

        # Set scale to max 1.
        new_scale = min(new_scale, 1)
        self.geometry.scale = (new_scale, new_scale)
