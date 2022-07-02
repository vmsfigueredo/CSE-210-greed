import random
from game.shared.point import Point
from game.shared.color import Color
from game.casting.artifact import Artifact

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, min_artifacts):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            min_artifacts (Number): The minimum quantity of the artifacts.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._min_artifacts = min_artifacts
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of players.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of players.
        """
        player = cast.get_first_player("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)
            

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of players.
        """
        banner = cast.get_first_player("banners")
        player = cast.get_first_player("players")
        artifacts = cast.get_players("artifacts")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for artifact in artifacts:
            fall = Point(0, 1)
            fall = fall.scale(player.get_score() * 0.5 * 10)
            
            artifact.make_fall(max_x, max_y)
            
            if (artifact.get_position().get_y == max_y):
                artifact.set_position(Point(random.randint(1, 60 - 1), 0))
            
            if (player.get_position().equals(artifact.get_position())):
                if (artifact.get_text() == chr(42)):
                    player.increase_score(1)
                else:
                    player.decrease_score(1)
                banner.set_text(f"Score: {player.get_score()}")
                cast.remove_player("artifacts", artifact)
        if(self._min_artifacts > len(artifacts)):
            text = chr(random.choice([79, 42]))
            
            x = random.randint(1, 60 - 1)
            y = 0
            position = Point(x, y)
            position = position.scale(15)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(15)
            artifact.set_color(color)
            artifact.set_position(position)
            cast.add_player("artifacts", artifact)
        
    def _do_outputs(self, cast):
        """Draws the players on the screen.
        
        Args:
            cast (Cast): The cast of players.
        """
        self._video_service.clear_buffer()
        players = cast.get_all_players()
        self._video_service.draw_players(players)
        self._video_service.flush_buffer()
    