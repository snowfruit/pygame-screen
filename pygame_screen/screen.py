"""This module provides a class that adds a foreground-surface on the screen-surface."""

import math

import pygame

from pygame_screen.fit import objectfit, surfacefit
from pygame_screen.geometry import Geometry
from pygame_screen.settings import Settings


class Screen:
    """Screen-class used for base. Not meant for direct use.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
    """

    def __init__(
        self, foreground_size: tuple = (320, 240), settings: Settings = Settings()
    ) -> None:
        # Try to get available display-surface.
        self.background = pygame.display.get_surface()
        """The background (alias screen/window)."""

        # Create a new one if not found.
        if self.background is None:
            self.background = pygame.display.set_mode(foreground_size, pygame.RESIZABLE)

        self._geometry = Geometry()
        """Foreground geometry. Scale, position, etc."""
        self._settings = settings
        """Screen settings. Clamping, colors, etc."""
        self._foreground: pygame.surface = pygame.Surface(foreground_size)
        """The foreground-surface."""
        self._foreground_scaled: pygame.surface = self.foreground.copy()
        """The scaled foreground-surface that blit onto foreground-surface."""

        self._adjust_settings()

    @property
    def settings(self) -> Settings:
        """Settings for the screen-class."""
        return self._settings

    @settings.setter
    def settings(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def geometry(self) -> Geometry:
        """Value can be be used for frame rate. Have no direct control over frame rate!"""
        return self._geometry

    @geometry.setter
    def geometry(self, geometry: Geometry) -> None:
        self._geometry = geometry

    @property
    def foreground(self) -> pygame.surface:
        """The foreground-surface."""
        return self._foreground

    @foreground.setter
    def foreground(self, surface: pygame.surface) -> None:
        self._foreground = surface

    @property
    def foreground_scaled(self) -> pygame.surface:
        """The foreground_scaled-surface."""
        return self._foreground_scaled

    @foreground_scaled.setter
    def foreground_scaled(self, surface: pygame.surface) -> None:
        self._foreground_scaled = surface

    def _adjust_settings(self):
        """Adjust settings after init if needed."""

    def clear(self) -> None:
        """Clear foreground-surface and screen-surface."""
        self.clear_foreground()
        self.clear_background()

    def clear_foreground(self) -> None:
        """Clear the surface. Fills foreground-surface with set color."""
        self.foreground.fill(self.settings.foreground_color)

    def clear_background(self) -> None:
        """Clear the surface. Fills screen-surface with set color."""
        self.background.fill(self.settings.screen_color)

    def update_scale(self) -> None:
        """Update variables relavant to scale."""
        # Calculate the scale-factor for the foreground-surface.
        self.geometry.scale = objectfit.ratio(
            self.background.get_size(), self.foreground.get_size()
        )

    def update(self) -> None:
        """Method that calls all relevant update-methods."""
        self.update_scale()
        self.update_position()

    def update_position(self) -> None:
        """Update variables relavant to position."""
        if self.settings.center_foreground:
            # scale = pygame.math.Vector2(self.geometry.scale)

            # Get the center-position for the screen-surface.
            # screen_center = pygame.math.Vector2(self.background.get_rect().center)
            screen_center_x, screen_center_y = self.background.get_rect().center

            # Get the center-position for the foreground-surface.
            foreground_center_x, foreground_center_y = self.foreground.get_rect().center

            # Add the wanted scale.
            foreground_center_x *= self.geometry.scale_x
            foreground_center_y *= self.geometry.scale_y

            # Calculate the new foreground-position.
            foreground_x: float = screen_center_x - foreground_center_x
            foreground_y: float = screen_center_y - foreground_center_y

            self.geometry.position = (foreground_x, foreground_y)

    def update_foreground_scaled(self) -> None:
        """Update the foreground_scaled-surface with new size."""
        # Method needs a better name.
        self.foreground_scaled = surfacefit.surface_scale_by(
            self.foreground, self.geometry.scale, self.settings.use_smooth_scaling
        )

    def blit_foreground_to_background(self) -> None:
        """Blit foreground-surface to background-surface."""
        # Everything should be done bliting to foreground-surface by now.

        # Scale the final foreground.
        self.update_foreground_scaled()

        # Blit the foreground-surface the screen-surface.
        self.background.blit(self.foreground_scaled, self.geometry.position)

    def get_mouse_position(self, clamp_size: bool = True) -> tuple[int, int]:
        """Get mouse-postion on the foreground-surface."""
        position: tuple[int, int] = self.position_background_to_foreground(
            pygame.mouse.get_pos(), clamp_size
        )

        return position

    def position_foreground_to_background(
        self, position: tuple, clamp_size: bool = True
    ) -> tuple[int, int]:
        """Covert foreground-coordinates to background-coordinates."""
        x: int = position[0]
        y: int = position[1]

        if clamp_size:
            # Clamp position to foreground-size.
            x = max(x, 0)
            y = max(y, 0)

            x = min(x, self.foreground.get_width())
            y = min(y, self.foreground.get_height())

        x = math.floor(x * self.geometry.scale_x)
        y = math.floor(y * self.geometry.scale_y)

        return (x, y)

    def position_background_to_foreground(
        self, position: tuple, clamp_size: bool = True
    ) -> tuple[int, int]:
        """Covert background-coordinates to foreground-coordinates."""
        x: int = math.floor(
            (position[0] - self.geometry.position[0]) / self.geometry.scale_x
        )
        y: int = math.floor(
            (position[1] - self.geometry.position[1]) / self.geometry.scale_y
        )

        if clamp_size:
            # Clamp position to foreground-size.
            x = max(x, 0)
            y = max(y, 0)

            x = min(x, self.foreground.get_width())
            y = min(y, self.foreground.get_height())

        return (x, y)
