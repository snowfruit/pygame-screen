"""Docstring."""

import pygame

from pygame_screen.screen import Screen

# Naming is done by matching css naming conventions.
# Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit


class ScreenMatch(Screen):
    """
    Based on Screen-class. With same sized canvas-surface and screen-surface.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
    """

    def update(self) -> None:
        # Make sure the canvas-surface and the screen-surface are the same size.
        if self.canvas.get_size() != self.screen.get_size():
            self.canvas = pygame.Surface(self.screen.get_size())

        # Late update. Needed to make sure scale is 1,1 and position 0,0.
        super().update()

    def update_scale(self) -> None:
        # 'Match' use a canvas-surface and screen-surface of the same size.
        # No scaling is done.
        self.geometry.scale = (1, 1)

    def update_position(self) -> None:
        # 'Match' always use 0, 0.
        self.geometry.position = (0, 0)

    def update_canvas_scaled(self) -> None:
        # 'Match' use a copy of the canvas-surface. No change in size is needed.
        self.canvas_scaled = self.canvas.copy()

    def position_canvas_to_screen(
        self, position: tuple, clamp_size: bool = True
    ) -> tuple[int, int]:
        # For 'match' the canvas-postion and screen-position are the same.
        return position

    def position_screen_to_canvas(
        self, position: tuple[int, int], clamp_size: bool = True
    ) -> tuple[int, int]:
        # For 'match' the canvas-postion and screen-position are the same.
        return position
