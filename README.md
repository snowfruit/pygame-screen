[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/snowfruit/pygame-screen/.github%2Fworkflows%2Fpylint.yml)
# pygame-screen
Add a responsive foreground-surface over an adaptive background-surface.
## Fit the canvas on screen
Different ways the foreground-surface can be placed on the background-surface.
* Center, fixed size
* Contain
* Cover
* Fill
* Fixed (position and size)
* Match (canvas-surface match screen-surface resolution)
* Scale-down
  
Read more about it here: https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
## Quick tutorial
### Install with pip (not ready)
pip install pygame-screen
### Install from source
Download 'pygame-screen'-directory and place in your project-folder.
### Example
From example_1.py.
```python
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
```
## Thanks to
* pygame https://github.com/pygame-community/pygame-ce
* Black https://github.com/psf/black
* isort https://github.com/PyCQA/isort
* GitHub https://github.com/
* pylint https://github.com/pylint-dev/pylint
* The Python Package Index https://pypi.org/
* ... and everyone else.
