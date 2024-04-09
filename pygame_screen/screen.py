"""This module provides a class that adds a canvas-surface on the screen-surface."""

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
        self, canvas_size: tuple = (320, 240), settings: Settings = Settings()
    ) -> None:
        # Try to get available display-surface.
        self.screen = pygame.display.get_surface()
        """The screen (alias background)."""

        # Create a new one if not found.
        if self.screen is None:
            self.screen = pygame.display.set_mode(canvas_size, pygame.RESIZABLE)

        self._geometry = Geometry()
        """Canvas geometry. Scale, position, etc."""
        self._settings = settings
        """Screen settings. Clamping, colors, etc."""
        self._canvas: pygame.surface = pygame.Surface(canvas_size)
        """The canvas (alias foreground)."""
        self._canvas_scaled: pygame.surface = self.canvas.copy()
        """The scaled canvas-surface that blit onto sceen-surface."""

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
    def canvas(self) -> pygame.surface:
        """The canvas-surface."""
        return self._canvas

    @canvas.setter
    def canvas(self, surface: pygame.surface) -> None:
        self._canvas = surface

    @property
    def canvas_scaled(self) -> pygame.surface:
        """The canvas_scaled-surface."""
        return self._canvas_scaled

    @canvas_scaled.setter
    def canvas_scaled(self, surface: pygame.surface) -> None:
        self._canvas_scaled = surface

    def _adjust_settings(self):
        """Adjust settings after init if needed."""

    def clear(self) -> None:
        """Clear canvas-surface and screen-surface."""
        self.clear_canvas()
        self.clear_screen()

    def clear_canvas(self) -> None:
        """Clear the surface. Fills canvas-surface with set color."""
        self.canvas.fill(self.settings.canvas_color)

    def clear_screen(self) -> None:
        """Clear the surface. Fills screen-surface with set color."""
        self.screen.fill(self.settings.screen_color)

    def update_scale(self) -> None:
        """Update variables relavant to scale."""
        # Calculate the scale-factor for the canvas-surface.
        self.geometry.scale = objectfit.ratio(
            self.screen.get_size(), self.canvas.get_size()
        )

    def update(self) -> None:
        """Method that calls all relevant update-methods."""
        self.update_scale()
        self.update_position()

    def update_position(self) -> None:
        """Update variables relavant to position."""
        if self.settings.center_canvas:
            # scale = pygame.math.Vector2(self.geometry.scale)

            # Get the center-position for the screen-surface.
            # screen_center = pygame.math.Vector2(self.screen.get_rect().center)
            screen_center_x, screen_center_y = self.screen.get_rect().center

            # Get the center-position for the canvas-surface.
            canvas_center_x, canvas_center_y = self.canvas.get_rect().center

            # Add the wanted scale.
            canvas_center_x *= self.geometry.scale_x
            canvas_center_y *= self.geometry.scale_y

            # Calculate the new canvas-position.
            # TODO: Is there a problem with rounding?
            canvas_x: int = math.floor(screen_center_x - canvas_center_x)
            canvas_y: int = math.floor(screen_center_y - canvas_center_y)

            self.geometry.position = (canvas_x, canvas_y)

    def update_canvas_scaled(self) -> None:
        """Update the canvas_scaled-surface with new size."""
        # TODO: Method needs a better name.
        self.canvas_scaled = surfacefit.surface_scale_by(
            self.canvas, self.geometry.scale, self.settings.use_smooth_scaling
        )

    def blit_canvas_to_screen(self) -> None:
        """Blit canvas-surface to screen-surface."""
        # Everything should be done bliting to canvas-surface by now.

        # Scale the final canvas.
        self.update_canvas_scaled()

        # Blit the canvas-surface the screen-surface.
        self.screen.blit(self.canvas_scaled, self.geometry.position)

    def get_mouse_position(self, clamp_size: bool = True) -> tuple[int, int]:
        """Get mouse-postion on the canvas-surface."""
        position: tuple[int, int] = self.position_screen_to_canvas(
            pygame.mouse.get_pos(), clamp_size
        )

        return position

    def position_canvas_to_screen(
        self, position: tuple, clamp_size: bool = True
    ) -> tuple[int, int]:
        """Covert canvas-coordinates to screen-coordinates."""
        x: int = position[0]
        y: int = position[1]

        if clamp_size:
            # clamp_size position to canvas-size.
            x = max(x, 0)
            y = max(y, 0)

            x = min(x, self.canvas.get_width())
            y = min(y, self.canvas.get_height())

        x = math.floor(x * self.geometry.scale_x)
        y = math.floor(y * self.geometry.scale_y)

        return (x, y)

    def position_screen_to_canvas(
        self, position: tuple, clamp_size: bool = True
    ) -> tuple[int, int]:
        """Covert screen-coordinates to canvas-coordinates."""
        x: int = math.floor(
            (position[0] - self.geometry.position[0]) / self.geometry.scale_x
        )
        y: int = math.floor(
            (position[1] - self.geometry.position[1]) / self.geometry.scale_y
        )

        if clamp_size:
            # clamp_size position to canvas-size.
            x = max(x, 0)
            y = max(y, 0)

            x = min(x, self.canvas.get_width())
            y = min(y, self.canvas.get_height())

        return (x, y)
