"""Please edit this docstring."""


class Geometry:
    """Geometry-class for the use in Screen-class."""

    def __init__(self) -> None:
        self._scale: tuple[float, float] = (1.0, 1.0)
        """Used for horizontal scaling on foreground and position."""

        self._zoom: tuple[float, float] = (1.0, 1.0)
        """Not implemented. Used for horizontal zoom on foreground and position."""

        self._position: tuple[float, float] = (0.0, 0.0)
        """Position the foreground-surface will be blit onto the screen-surface."""

    @property
    def scale(self) -> tuple[float, float]:
        """'Scale' as tuple."""
        return self._scale

    @scale.setter
    def scale(self, factor: tuple[float, float]) -> None:
        self._scale = factor

    @property
    def scale_x(self) -> float:
        """Value used for horizontal scaling."""
        return self._scale[0]

    @scale_x.setter
    def scale_x(self, factor: float) -> None:
        self._scale = (factor, self.scale_y)

    @property
    def scale_y(self) -> float:
        """Value used for vertical scaling."""
        return self._scale[1]

    @scale_y.setter
    def scale_y(self, factor: float) -> None:
        self._scale = (self.scale_y, factor)

    @property
    def zoom(self) -> tuple[float, float]:
        """'Zoom' as tuple."""
        return self._zoom

    @zoom.setter
    def zoom(self, value: tuple[float, float]) -> None:
        self._zoom = value

    @property
    def zoom_x(self) -> float:
        """Value used for horizontal zoom."""
        return self._zoom_x

    @zoom_x.setter
    def zoom_x(self, value: float) -> None:
        self._zoom_x = value

    @property
    def zoom_y(self) -> float:
        """Value used for vertical zoom."""
        return self._zoom_y

    @zoom_y.setter
    def zoom_y(self, value: float) -> None:
        self._zoom_y = value

    @property
    def position(self) -> tuple[float, float]:
        """The position foreground-surface is blit on screen-surface."""
        return self._position

    @position.setter
    def position(self, value: tuple[float, float]) -> None:
        self._position = value

    @property
    def position_x(self) -> float:
        """Value used for horizontal position."""
        return self._position[0]

    @position_x.setter
    def position_x(self, position: float) -> None:
        self._position = (position, self.position_y)

    @property
    def position_y(self) -> float:
        """Value used for vertical position."""
        return self._position[1]

    @position_y.setter
    def position_y(self, position: float) -> None:
        self._position = (self.position_x, position)
