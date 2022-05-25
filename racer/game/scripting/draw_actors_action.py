from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("scores1")
        score2 = cast.get_first_actor("scores2")
        cycle1 = cast.get_first_actor("cycle1")
        segments1 = cycle1.get_segments()

        cycle2 = cast.get_first_actor("cycle2")
        segments2 = cycle2.get_segments()
        messages = cast.get_actors("messages")

        prize = cast.get_first_actor("prize")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actor(prize)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()