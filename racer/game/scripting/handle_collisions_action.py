import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_cycle_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_cycle_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        head1 = cycle1.get_head()
        head2 = cycle2.get_head()

        score1 = cast.get_first_actor("scores1")
        score2 = cast.get_first_actor("scores2")

        prize = cast.get_first_actor("prize")

        if head1.get_position().equals(prize.get_position()):
            score1.add_points1(1)
            prize.reset()

            if score1.get_points1() == 5:
                self._is_game_over = True

        if head2.get_position().equals(prize.get_position()):
            score2.add_points2(1)
            prize.reset()

            if score2.get_points2() == 5:
                self._is_game_over = True

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]

        cycle2 = cast.get_first_actor("cycle2")
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        
        for segment in segments1:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in segments2:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True

        
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycle1")
            segments1 = cycle1.get_segments()

            cycle2 = cast.get_first_actor("cycle2")
            segments2 = cycle2.get_segments()

            prize = cast.get_first_actor("prize")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            score1 = cast.get_first_actor("scores1")
            score2 = cast.get_first_actor("scores2")

            message = Actor()
            if score2.get_points2() == 5:
                message.set_text("Racer 2 Wins!")
            else:
                message.set_text("Racer 1 Wins")
            message.set_position(position)
            cast.add_actor("messages", message)

            prize.set_color(constants.WHITE)

            for segment in segments1:
                segment.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)