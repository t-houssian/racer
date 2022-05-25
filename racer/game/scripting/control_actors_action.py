import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction1(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)

            if self._keyboard_service.is_key_up('a'):    
                cycle1 = cast.get_first_actor("cycle1")
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)

            if self._keyboard_service.is_key_up('d'):
                cycle1 = cast.get_first_actor("cycle1")                
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            
            if self._keyboard_service.is_key_up('w'):
                cycle1 = cast.get_first_actor("cycle1")
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            
            if self._keyboard_service.is_key_up('s'):
                cycle1 = cast.get_first_actor("cycle1")

        cycle1 = cast.get_first_actor("cycle1")
        cycle1.turn_head(self._direction)


class ControlActorsAction2(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('left'):
            self._direction = Point(-constants.CELL_SIZE, 0)

            if self._keyboard_service.is_key_up('left'):
                cycle2 = cast.get_first_actor("cycle2")
        
        # right
        if self._keyboard_service.is_key_down('right'):
            self._direction = Point(constants.CELL_SIZE, 0)
            
            if self._keyboard_service.is_key_up('right'):
                cycle2 = cast.get_first_actor("cycle2")
        
        # up
        if self._keyboard_service.is_key_down('up'):
            self._direction = Point(0, -constants.CELL_SIZE)
            
            if self._keyboard_service.is_key_up('up'):
                cycle2 = cast.get_first_actor("cycle2")
        
        # down
        if self._keyboard_service.is_key_down('down'):
            self._direction = Point(0, constants.CELL_SIZE)
            
            if self._keyboard_service.is_key_up('down'):
                cycle2 = cast.get_first_actor("cycle2")

        cycle2 = cast.get_first_actor("cycle2")
        cycle2.turn_head(self._direction)