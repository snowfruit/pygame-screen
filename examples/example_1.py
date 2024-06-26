"""
Example 1.
Showing the background-surface contained inside the foreground-surface.
"""

import pygame

from pygame_screen import ScreenContain


def main():
    """Function running the example."""
    pygame.init()
    clock = pygame.Clock()

    # Window, screen and canvas use the same size in this example.
    window_size = (320, 240)
    # Set everything to the same size.
    screen = ScreenContain(window_size)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the screen. Size, scale and everything else.
        screen.update()
        # Fill canvas-surface and screen-surface with set colors.
        screen.clear()

        # Render a circle to help demonstrate the scaling.
        pygame.draw.circle(screen.foreground, (255, 255, 255), (160, 120), 32)

        # Blit canvas-surface to screen-surface.
        screen.blit_foreground_to_background()

        pygame.display.flip()

        clock.tick(screen.settings.frame_rate)

    pygame.quit()


if __name__ == "__main__":
    main()
