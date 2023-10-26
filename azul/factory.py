from miss.prints import Prints

class Factory:
        def __init__(self, num_players):
                if num_players == 2:
                        self.factory_displays = [[], [], [], [], []]
                elif num_players == 3:
                        self.factory_displays = [[], [], [], [], [], [], []]
                elif num_players == 4:
                        self.factory_displays = [[], [], [], [], [], [], [], [], []]
        
        def get_tiles_from_display(self, choiceColor, choiceDisplay, players, current_player, garbage, starter_tile):
                tiles_picked = []
                if any(tile.color == choiceColor for tile in self.factory_displays[choiceDisplay-1]):                
                        for tile in self.factory_displays[choiceDisplay-1]:
                                if tile.color == choiceColor:
                                        tiles_picked.append(tile) #the user gets the tiles from that color
                                else:
                                        garbage.append(tile) #the rest of the tiles go to garbage
                                if players[current_player].starter_tile == starter_tile: #if the players still ahve the starter tile (his first move) the tile goes to garbage
                                        garbage.append(starter_tile)
                                        players[current_player].starter_tile = None
                        self.factory_displays[choiceDisplay-1] = [] #clear the factory display
                        if players[current_player].starter_tile is not None: #if the current player is the first on this round, he puts the starter tile on gargabe
                                starter_t = players[current_player].starter_tile
                                garbage.append(starter_t)
                                players[current_player].starter_tile = None  
                        return tiles_picked
                else:
                        print("The chosen display doesn't contain this color")
                return None

        def validade_color_in_line(self, choiceColor, choiceDisplay):
                if any(tile.color == choiceColor for tile in self.factory_displays[choiceDisplay-1]):
                        return True
                else:
                        print("The chosen display doesn't contain this color") 
                        return False      


        def validate_chosen_display(self):
                while True:
                        choiceDisplay = input()
                        choiceDisplay = int(choiceDisplay)  # Convert the input to an integer
                        if 1 <= choiceDisplay <= len(self.factory_displays):
                                if len(self.factory_displays[choiceDisplay-1]) == 0:
                                         print("This factory is empty. Please choose another one")
                                else:
                                        return choiceDisplay
                        else:
                                print(f"Invalid input. Please enter a number between 1 and {len(self.factory_displays)}.")

        def print_factories(self):
                count = 1
                x = 0
                for f in self.factory_displays:
                        print('factory ' + str(count) + ': ')
                        count = count + 1
                        if len(f) == 0:
                                print("_ _ _ _")
                        else:                
                                x = 0
                                for i in range(4):
                                        x = x + 1
                                        if f[i] is not None:
                                                Prints.print_colored_text_with_square(f[i].color, x)
                                        else: 
                                                print("_")