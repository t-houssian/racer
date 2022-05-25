import os
import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color

class Prize(Actor):
    """
    An prize for the racers.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.set_text("$")
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # color = Color(r, g, b)
        color = constants.BLUE
        self.set_color(color)
        self.reset()

    def reset(self):
        """Selects a random position and points that the food is worth."""
        self._points = 1
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points