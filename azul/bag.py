from .tile import Tile  # Import the Tile class
import random 

class Bag:
    def __init__(self):
        # Define the 5 colors available
        colors = ["blue", "orange", "red", "black", "white"]
        
        # Create 20 tiles of each color
        self.tiles = []
        for color in colors:
            for _ in range(20):
                self.tiles.append(Tile(color))
        # Shuffle the tiles
        random.shuffle(self.tiles)

    def draw_tile(self):
        # Implement the logic to draw a tile from the bag
        if self.tiles:
            return self.tiles.pop()
        else:
            return None  # Return None if the bag is empty
        
