import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Score1(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points1 = 0
        self.add_points1(0)
        self._position = Point(constants.MAX_X, constants.MAX_Y)

    def add_points1(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points1 += points
        self.set_text(f"Player One: {self._points1}")

    def get_points1(self):
        """Gets the points the prize is worth.
        
        Returns:
            points (int): The points the prize is worth.
        """
        return self._points1


class Score2(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points2 = 0
        self.add_points2(0)
        self._position = Point(770, 0)


    def add_points2(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points2 += points
        self.set_text(f"Player Two: {self._points2}")

    def get_points2(self):
        """Gets the points the prize is worth.
        
        Returns:
            points (int): The points the prize is worth.
        """
        return self._points2