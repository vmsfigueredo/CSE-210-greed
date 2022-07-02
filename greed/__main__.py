import os
import random
import time

from game.casting.player import Player
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 30
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 300
OBJ = [79, 42]

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Player()
    banner.set_text("Score: 0 ")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_player("banners", banner)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - 30)
    position = Point(x, y)

    player = Player()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_player("players", player)
    
    # create the artifacts

    for n in range(DEFAULT_ARTIFACTS):
        text = chr(random.choice(OBJ))

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 5)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_player("artifacts", artifact)
            
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, DEFAULT_ARTIFACTS)
    director.start_game(cast)
    

if __name__ == "__main__":
    main()