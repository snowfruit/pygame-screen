"""Docstring."""

from pygame_screen.screen import Screen, surfacefit

# Naming is done by matching css naming conventions.
# Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit


class ScreenFill(Screen):
    """
    Based on Screen-class. Applies a fill-style to canvas-surface.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit#fill
    """

    def update_position(self) -> None:
        # 'Fill' always use 0, 0.
        self.geometry.position = (0, 0)

    def update_canvas_scaled(self) -> None:
        # Resize to new resolution.
        new_size = self.screen.get_size()

        self.canvas_scaled = surfacefit.surface_resize_to(
            self.canvas, new_size, self.settings.use_smooth_scaling
        )
