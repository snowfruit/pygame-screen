"""Please edit this docstring."""

import pygame

from pygame_screen.screen import Screen

# Naming is done by matching css naming conventions.
# Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit


class ScreenMatch(Screen):
    """
    Based on Screen-class. With same sized foreground-surface and screen-surface.
    Note:
        https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
    """

    def update(self) -> None:
        # Make sure the foreground-surface and the screen-surface are the same size.
        if self.foreground.get_size() != self.background.get_size():
            self.foreground = pygame.Surface(self.background.get_size())

        # Late update. Needed to make sure scale is 1,1 and position 0,0.
        super().update()

    def update_scale(self) -> None:
        # 'Match' use a foreground-surface and screen-surface of the same size.
        # No scaling is done.
        self.geometry.scale = (1, 1)

    def update_position(self) -> None:
        # 'Match' always use 0, 0.
        self.geometry.position = (0, 0)

    def update_foreground_scaled(self) -> None:
        # 'Match' use a copy of the foreground-surface. No change in size is needed.
        self.foreground_scaled = self.foreground.copy()

    def position_foreground_to_background(
        self, position: tuple, clamp_size: bool = True
    ) -> tuple[int, int]:
        # For 'match' the foreground-postion and screen-position are the same.
        return position

    def position_background_to_foreground(
        self, position: tuple[int, int], clamp_size: bool = True
    ) -> tuple[int, int]:
        # For 'match' the foreground-postion and screen-position are the same.
        return position
