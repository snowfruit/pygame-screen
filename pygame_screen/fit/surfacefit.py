"""Function for fitting options. Naming is done by matching css naming conventions.
Note:
    https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
"""

import pygame.transform

from pygame_screen.fit import objectfit


def surface_resize_to(
    surface: pygame.surface,
    size: tuple[float, float],
    use_smooth_scaling: bool = False,
) -> pygame.surface:
    """Docstring."""
    if use_smooth_scaling:
        return pygame.transform.smoothscale(surface, size)

    return pygame.transform.scale(surface, size)


def surface_scale_by(
    surface: pygame.surface,
    factor: tuple[float, float],
    use_smooth_scaling: bool = False,
) -> pygame.surface:
    """Docstring."""
    if use_smooth_scaling:
        return pygame.transform.smoothscale_by(surface, factor)

    return pygame.transform.scale_by(surface, factor)


def surface_sizes(surface_a, surface_b) -> tuple[tuple[int, int], tuple[int, int]]:
    """Get tuple's with sizes from surfaces."""
    size_a = ...
    size_b = ...

    if isinstance(surface_a, pygame.Surface):
        size_a = surface_a.get_size()
    else:
        size_a = surface_a

    if isinstance(surface_b, pygame.Surface):
        size_b = surface_b.get_size()
    else:
        size_b = surface_b

    return (size_a, size_b)


def surface_contain(
    surface_a,
    surface_b,
    use_integer_scaling: bool = False,
    use_smooth_scaling: bool = False,
    clamp: bool = False,
) -> pygame.surface:
    """Docstring."""
    size_a, size_b = surface_sizes(surface_a, surface_b)
    scale = objectfit.resize_contain(size_a, size_b, use_integer_scaling, clamp)
    return surface_scale_by(surface_a, scale, use_smooth_scaling)


def surface_cover(
    surface_a,
    surface_b,
    use_integer_scaling: bool = False,
    use_smooth_scaling: bool = False,
    clamp: bool = False,
) -> pygame.surface:
    """Docstring."""
    size_a, size_b = surface_sizes(surface_a, surface_b)
    scale = objectfit.resize_cover(size_a, size_b, use_integer_scaling, clamp)
    return surface_scale_by(surface_a, scale, use_smooth_scaling)


def surface_fill(
    surface_a,
    surface_b,
    use_integer_scaling: bool = False,
    use_smooth_scaling: bool = False,
    clamp: bool = False,
) -> pygame.surface:
    """Docstring."""
    size_a, size_b = surface_sizes(surface_a, surface_b)
    scale = objectfit.resize_fill(size_a, size_b, use_integer_scaling, clamp)
    return surface_scale_by(surface_a, scale, use_smooth_scaling)


def surface_scale_down(
    surface_a,
    surface_b,
    use_integer_scaling: bool = False,
    use_smooth_scaling: bool = False,
    clamp: bool = False,
) -> pygame.surface:
    """Docstring."""
    size_a, size_b = surface_sizes(surface_a, surface_b)
    scale = objectfit.resize_scale_down(size_a, size_b, use_integer_scaling, clamp)
    return surface_scale_by(surface_a, scale, use_smooth_scaling)


def surface_match(
    surface_a,
    surface_b,
    use_integer_scaling: bool = False,
    use_smooth_scaling: bool = False,
    clamp: bool = False,
) -> pygame.surface:
    """Docstring."""
    _, size_b = surface_sizes(surface_a, surface_b)

    new_size = objectfit.resize_match(size_b, use_integer_scaling, clamp)

    return surface_resize_to(surface_a, new_size, use_smooth_scaling)
