import constants

from game.casting.cast import Cast
from game.casting.score import Score1, Score2
from game.casting.cycle import Cycle1, Cycle2
from game.casting.prize import Prize
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction1, ControlActorsAction2
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cycle1", Cycle1())
    cast.add_actor("cycle2", Cycle2())
    cast.add_actor("scores1", Score1())
    cast.add_actor("scores2", Score2())
   
    cast.add_actor("prize", Prize())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction1(keyboard_service))
    script.add_action("input", ControlActorsAction2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()