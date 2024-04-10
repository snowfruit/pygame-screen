"""Example 1. Showing the canvas-surface contained inside the screen-surface."""

import pygame

from pygame_screen import ScreenContain


def main():
    """Function running the example."""
    pygame.init()
    clock = pygame.Clock()

    # Window, screen and canvas use the same size in this example.
    window_size = (320, 240)
    # Use a screen set to contain the canvas.
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
        pygame.draw.circle(screen.canvas, (255, 255, 255), (160, 120), 32)

        # Blit canvas-surface to screen-surface.
        screen.blit_canvas_to_screen()

        pygame.display.flip()

        clock.tick(screen.settings.frame_rate)

    pygame.quit()


if __name__ == "__main__":
    main()
