"""Please edit this docstring."""

import pygame.color


class Settings:
    """Settings-class for use with Screen-class."""

    def __init__(self) -> None:
        self._frame_rate: float = 30.0
        """Value can be be used for frame rate. Have no direct control over frame rate!"""

        self._use_integer_scaling: bool = False
        """Scale foreground using integer instead of float?"""

        self._use_smooth_scaling: bool = False
        """Scale foreground using bilinear scaling?"""

        self._center_foreground: bool = True
        """Center the foreground-surface on the screen-surface?"""

        self._clamp_size: bool = True
        """Clamp minimum size to the foreground original size."""

        # Fill colors.
        self._foreground_color: pygame.color = (0, 128, 0)  # Dark green.
        """Fill-color used when clearing the foreground-surface."""
        self._background_color: pygame.color = (128, 0, 0)  # Dark red.
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
        """Clamp minimum size to the foreground original size."""
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
        """Resize using bilinear filter on foreground-surface."""
        return self._use_smooth_scaling

    @use_smooth_scaling.setter
    def use_smooth_scaling(self, value: bool) -> None:
        self._use_smooth_scaling = value

    @property
    def center_foreground(self) -> bool:
        """Center foreground-surface over screen-surface."""
        return self._center_foreground

    @center_foreground.setter
    def center_foreground(self, value: bool) -> None:
        self._center_foreground = value

    @property
    def foreground_color(self) -> pygame.color:
        """Color used when filling the foreground-surface when cleared."""
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, color: pygame.color) -> None:
        self._foreground_color = color

    @property
    def screen_color(self) -> pygame.color:
        """Color used when filling the background-surface when cleared."""
        return self._background_color

    @screen_color.setter
    def screen_color(self, color: pygame.color) -> None:
        self._background_color = color
