"""Function for fitting options. Naming is done by matching css naming conventions.
Note:
    https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
"""

import math

# from typing import Optional
# from enum import Enum


def ratio(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    """Docstring."""
    x = a[0] / b[0]
    y = a[1] / b[1]

    return (x, y)


def resize_contain(
    size_a: tuple[float, float],
    size_b: tuple[float, float],
    use_integer_scaling: bool = False,
    clamp: bool = False,
) -> tuple[float, float]:
    """Docstring."""
    scale_x, scale_y = ratio(size_a, size_b)
    new_scale = min(scale_x, scale_y)

    # Set scale to a minimum of 1 if clamped.
    if clamp:
        new_scale = max(new_scale, 1)

    if use_integer_scaling:
        # Set scale to a minimum of 1. Else it could be 0.
        new_scale = max(new_scale, 1)
        new_scale = math.floor(new_scale)

    # Set scale_x and scale_y to the same value.
    return (new_scale, new_scale)


def resize_cover(
    size_a: tuple[float, float],
    size_b: tuple[float, float],
    use_integer_scaling: bool = False,
    clamp: bool = False,
) -> tuple[float, float]:
    """Docstring."""
    scale_x, scale_y = ratio(size_a, size_b)

    # 'Cover' needs scale_x and scale_y to be the same value.
    # Set scale to the biggest of width and height.
    new_scale = max(scale_x, scale_y)

    # Set scale to a minimum of 1 if clamped.
    if clamp:
        new_scale = max(new_scale, 1)

    if use_integer_scaling:
        # Set scale to a minimum of 1. Else it could be 0.
        new_scale = max(new_scale, 1)
        new_scale = math.ceil(new_scale)

    # Set scale_x and scale_y to the same value.
    return (new_scale, new_scale)


def resize_fill(
    size_a: tuple[float, float],
    size_b: tuple[float, float],
    use_integer_scaling: bool = False,
    clamp: bool = False,
) -> tuple[float, float]:
    """Docstring."""
    scale_x, scale_y = ratio(size_a, size_b)

    # Set scale to a minimum of 1 if clamped.
    if clamp:
        scale_x = max(scale_x, 1)
        scale_y = max(scale_y, 1)

    if use_integer_scaling:
        # Set scale to a minimum of 1. Else it could be 0.
        scale_x = max(scale_x, 1)
        scale_y = max(scale_y, 1)

        scale_x = math.floor(scale_x)
        scale_y = math.floor(scale_y)

    # Set scale_x and scale_y to the same value.
    return (scale_x, scale_y)


def resize_scale_down(
    size_a: tuple[float, float],
    size_b: tuple[float, float],
    use_integer_scaling: bool = False,
    clamp: bool = False,
) -> tuple[float, float]:
    """Docstring."""
    # Scale-down is the same base as contain.

    return resize_contain(size_a, size_b, use_integer_scaling, clamp)


def resize_match(
    size: tuple[float, float],
    use_integer_scaling: bool = False,
    clamp: bool = False,
) -> tuple[float, float]:
    """Docstring."""
    x, y = size

    if use_integer_scaling:
        x = math.floor(x)
        y = math.floor(y)

        # If scaling is used then clamp is needed.
        clamp = True

    if clamp:
        x = max(x, 1)
        y = max(y, 1)

    return (x, y)
