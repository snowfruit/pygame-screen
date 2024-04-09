from random import random, randrange
import pygame
from pygame_screen import *


def main():
    pygame.init()
    clock = pygame.Clock()

    # Window, screen and canvas use the same size in this example.
    window_size = (320, 240)

    # Screen use a resizable window.
    # It's not necessary to create a window here but possible.
    # screen_not_needed = pygame.display.set_mode(window_size, pygame.RESIZABLE)

    # Settings we can use to make things easier to change.

    # A retro, blocky settings-object.
    retro = Settings()
    retro.use_integer_scaling = True
    retro.use_smooth_scaling = False

    # A modern, smooth settings-object.
    modern = Settings()
    modern.use_integer_scaling = False
    modern.use_smooth_scaling = True

    # Set canvas-size to same as starting screen-size.
    # Use a screen set to contain the canvas.
    screen = ScreenContain(window_size)

    pygame.display.set_caption(screen.__class__.__name__)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Different screen preset to try.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    screen = ScreenContain(window_size, retro)
                if event.key == pygame.K_2:
                    screen = ScreenContain(window_size, modern)
                if event.key == pygame.K_3:
                    screen = ScreenCover(window_size, retro)
                if event.key == pygame.K_4:
                    screen = ScreenCover(window_size, modern)
                if event.key == pygame.K_5:
                    screen = ScreenFill(window_size, retro)
                if event.key == pygame.K_6:
                    screen = ScreenFill(window_size, modern)
                if event.key == pygame.K_7:
                    screen = ScreenScaleDown(window_size, retro)
                if event.key == pygame.K_8:
                    screen = ScreenScaleDown(window_size, modern)
                if event.key == pygame.K_q:
                    # Create a ScreemFixed with random scale and position.
                    screen = ScreenFixed(window_size)

                    # Set new random scale.
                    screen.geometry.scale_x = 0.5 + random()
                    screen.geometry.scale_y = 0.5 + random()

                    # Set new random position.
                    x = randrange(window_size[0])
                    y = randrange(window_size[1])
                    screen.geometry.position = (x, y)
                if event.key == pygame.K_w:
                    # Create a ScreemFixedCenter with random scale.
                    screen = ScreenCenterFixedSize(window_size)

                    # Set new random scale.
                    screen.geometry.scale_x = 0.5 + random()
                    screen.geometry.scale_y = 0.5 + random()
                if event.key == pygame.K_e:
                    screen = ScreenMatch(window_size)

                print(screen.__class__.__name__)
                pygame.display.set_caption(screen.__class__.__name__)

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
