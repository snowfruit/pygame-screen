"""Docstring."""

import pygame.color


class Settings:
    """Settings-class for use with Screen-class."""

    def __init__(self) -> None:
        self._frame_rate: float = 30.0
        """Value can be be used for frame rate. Have no direct control over frame rate!"""

        self._use_integer_scaling: bool = False
        """Scale canvas using integer instead of float?"""

        self._use_smooth_scaling: bool = False
        """Scale canvas using bilinear scaling?"""

        self._center_canvas: bool = True
        """Center the canvas-surface on the screen-surface?"""

        self._clamp_size: bool = True
        """Clamp minimum size to the canvas original size."""

        # Fill colors.
        self._canvas_color: pygame.color = (0, 128, 0)  # Dark green.
        """Fill-color used when clearing the canvas-surface."""
        self._screen_color: pygame.color = (128, 0, 0)  # Dark red.
        """Fill-color used when clearing the screen-surface."""

    @property
    def frame_rate(self) -> float:
        """Value can be be used for frame rate. Have no direct control over frame rate!"""
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate: float) -> None:
        self._frame_rate = frame_rate

    @property
    def clamp_size(self) -> bool:
        """Clamp minimum size to the canvas original size."""
        return self._clamp_size

    @clamp_size.setter
    def clamp_size(self, clamp_size: bool) -> None:
        self._clamp_size = clamp_size

    @property
    def use_integer_scaling(self) -> bool:
        """Resize using integer scale-values."""
        return self._use_integer_scaling

    @use_integer_scaling.setter
    def use_integer_scaling(self, value: bool) -> None:
        self._use_integer_scaling = value

    @property
    def use_smooth_scaling(self) -> bool:
        """Resize using bilinear filter on canvas-surface."""
        return self._use_smooth_scaling

    @use_smooth_scaling.setter
    def use_smooth_scaling(self, value: bool) -> None:
        self._use_smooth_scaling = value

    @property
    def center_canvas(self) -> bool:
        """Center canvas-surface over screen-surface."""
        return self._center_canvas

    @center_canvas.setter
    def center_canvas(self, value: bool) -> None:
        self._center_canvas = value

    @property
    def canvas_color(self) -> pygame.color:
        """Color used when filling the canvas-surface when cleared."""
        return self._canvas_color

    @canvas_color.setter
    def canvas_color(self, color: pygame.color) -> None:
        self._canvas_color = color

    @property
    def screen_color(self) -> pygame.color:
        """Color used when filling the screen-surface when cleared."""
        return self._screen_color

    @screen_color.setter
    def screen_color(self, color: pygame.color) -> None:
        self._screen_color = color
