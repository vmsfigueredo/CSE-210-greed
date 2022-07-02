from game.casting.player import Player
from game.shared.point import Point

class Artifact(Player):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        
    def make_fall(self, max_x, max_y):
        """Make the artifacts fall

        Args:
            max_x (number): Maximum X
            max_y (number): Maximum Y
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y + 1
        self._position = Point(x, y)