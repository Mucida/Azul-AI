class Board:   

    def __init__(self):
        self.lines = [[], [], [], [], []]
        self.wall = [[None, None, None, None, None],
                     [None, None, None, None, None],
                     [None, None, None, None, None],
                     [None, None, None, None, None],
                     [None, None, None, None, None]]
        self.broken = [None] * 7
        # Fill lines with placeholders for 1 to 5 tiles
        for i in range(1, 6):
            self.lines[i - 1] = [None] * i


    def place_tile_on_wall(self, row, col, tile):
        # Action to place a tile on the board itself
        if self.rows[row][col] == '':
            for tile_in_row in self.rows[row]:
                if tile_in_row == tile.color:
                    raise ValueError("Invalid placement. Tile with the same color is already in this row.")
            self.rows[row][col] = tile.color
        else:
            raise ValueError("Invalid placement. Tile already exists in this location.")


    def insert_tile_in_line(self, color, choice_line, tiles_picked, players, current_player):
        for tile in players[current_player].board.lines[choice_line-1]:
            if tile is not None:
                print("tile color: " + tile.color)
                print("color: " + color)   
            if tile is not None and tile.color != color:
                print("You have another tile color in this line, chose another")
                return False
            else:                  
                while tiles_picked and None in players[current_player].board.lines[choice_line-1]:
                    tile = tiles_picked.pop()  # Get a tile from 'tiles_picked'
                    spot_index = players[current_player].board.lines[choice_line-1].index(None)  # Find an empty spot
                    players[current_player].board.lines[choice_line-1][spot_index] = tile  # Place the tile in the empty spot
                if len(tiles_picked) > 0: #get the extra tiles and put them in the broken tiles pile
                    while len(tiles_picked) > 0:
                        tile = tiles_picked.pop()
                        players[current_player].board.broken.append(tile)
                return True
            

    def score_board(self):
        # Action to score the board based on patterns and completed rows/columns
        # Implement scoring logic
        pass


    