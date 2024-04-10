"""Please edit this docstring."""

from pygame_screen.screen import Screen, surfacefit

# Naming is done by matching css naming conventions.
# Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit


class ScreenFill(Screen):
    """
    Based on Screen-class. Applies a fill-style to foreground-surface.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit#fill
    """

    def update_position(self) -> None:
        # 'Fill' always use 0, 0.
        self.geometry.position = (0, 0)

    def update_foreground_scaled(self) -> None:
        # Resize to new resolution.
        new_size = self.background.get_size()

        self.foreground_scaled = surfacefit.surface_resize_to(
            self.foreground, new_size, self.settings.use_smooth_scaling
        )
