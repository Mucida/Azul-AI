from .board import Board
from .tile import Tile

class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = []  # The tiles a player has chosen
        self.starter_tile = None
        self.score = 0
        self.board = Board()