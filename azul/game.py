from .player import Player
from .board import Board
from .bag import Bag
from .factory import Factory
from .tile import Tile
from miss.prints import Prints

import random

class AzulGame:

    #fill the factories displays with 4 tiles on it
    def fill_factory(self):
        for f in self.factory.factory_displays:
            for i in range(4):
                tile = self.bag.draw_tile()  # Draw a tile from the bag
                if tile is not None:
                    f.append(tile)  # Add the drawn tile to the current factory display


    #initial configurations to start the game
    def __init__(self, num_players):
        self.players = [Player(f"Player {i + 1}") for i in range(num_players)]
        self.boards = [Board() for _ in range(num_players)]
        self.factory = Factory(num_players)
        self.bag = Bag() #start a new bag with the 100 tiles on it
        self.garbage = [] #initiate an empty garbage (a list of tiles)
        self.start_tile_number = random.randint(0, num_players - 1) # Generate a random number to get the starter tile
        self.current_player = self.start_tile_number #the player with the index number gets the starter tile and will start the game
        self.starter_tile = Tile('start')
        self.players[self.current_player].starter_tile = self.starter_tile #gives the starter tile to the player who will start the game
        self.round = 1
        self.prints = Prints()

        for i, player in enumerate(self.players):
            player.board = self.boards[i] #each players get its own board

        self.fill_factory() #put the first 4 tiles in the factory displays
        self.factory.print_factories()
        
    
    #check if the input matches with any color availabel. Then pull the tiles from the display.
    def validade_chosen_color(self):
        valid_colors = {"b": "black", "u": "blue", "w": "white", "o": "orange", "r": "red"}
        while True:
            choiceColor = input()
            choiceColor = valid_colors.get(choiceColor, None)  # Get the full color name based on the user's choice
            if choiceColor:
                return choiceColor             
            else:
                print('Choose one of the following colors: "b": "black", "u": "blue", "w": "white", "o": "orange", "r": "red"')

    #check if there is any spot on this line and if the colors matches. Then insert the tiles
    def check_line_availability(self, choice_line, color, tiles_picked):
        if all(tile is not None for tile in self.players[self.current_player].board.lines[choice_line-1]):
            print("This line is full. Please chose another line")
            return False
        else:
            result =  self.players[self.current_player].board.insert_tile_in_line(color, choice_line, tiles_picked, self.players, self.current_player)
            if not result:
                return False  
        self.prints.print_current(choice_line, self.garbage, self.players, self.current_player, self.factory)
        return True



    #check if its a valid input and then check if the line is available
    def validate_chosen_line(self, tiles_picked):
        while True:
            choiceLine = input()
            choiceLine = int(choiceLine)
            color = tiles_picked[0].color
            if 1 <= choiceLine <= 5:
                return choiceLine, color
            else: 
                print("Please enter a number between 1 and 5")
                

    #check if the players' lines are not full, so he can buy from factories.
    def check_lines_availability(self):
        for i, line in enumerate(self.players[self.current_player].board.lines, start=1):
            for x in range(0,i):
                if line[x] == None:
                    return True
        return False


    def buy_from_factory(self):
        if not self.check_lines_availability():
            print("You cant buy from factory anymore, your lines are full")
            return False
        
        print(f'From which factory display do you want to buy? (1 to {len(self.factory.factory_displays)})')
        choiceDisplay = self.factory.validate_chosen_display()
        
        while True:
            print("What color do you want to buy? (b-black, u-blue, w-white, o-orange, r-red)")
            choiceColor = self.validade_chosen_color()
            if self.factory.validade_color_in_line(choiceColor, choiceDisplay): break
        tiles_picked = self.factory.get_tiles_from_display(choiceColor, choiceDisplay, self.players, self.current_player, self.garbage, self.starter_tile)
            
        while True:
            print("In which line you want to put your(s) " + tiles_picked[0].color + " tile(s) (1 to 5)")
            choiceLine, color = self.validate_chosen_line(tiles_picked)
            result = self.check_line_availability(choiceLine, color, tiles_picked)
            if result: break
        return True       

    def get_tiles_from_garbage(self, choiceColor):
        tiles_picked = [] 
        tiles_to_remove = []  # Create a list to store tiles to remove       
        if any(tile.color == choiceColor for tile in self.garbage):                           
            for tile in self.garbage:
                if tile.color == 'start':
                    self.players[self.current_player].board.broken.append(tile)
                    tiles_to_remove.append(tile)
                    continue                       
                if tile.color == choiceColor:
                    tiles_picked.append(tile) #the user gets the tiles from that color
                    tiles_to_remove.append(tile)
            # Remove marked tiles
            for tile in tiles_to_remove:
                self.garbage.remove(tile)                
            return tiles_picked
        else:
            print("This color is not on the garbage. Please choose another.")
            return None


    def buy_from_garbage(self):
        if len(self.garbage) == 0 or (len(self.garbage) == 1 and self.garbage[0].color == 'start'):
            print("The garbage is empty.")
            return False     
        self.prints.print_garbage(self.garbage)

        while True:
            print("What color do you want to buy? (b-black, u-blue, w-white, o-orange, r-red)")
            choiceColor = self.validade_chosen_color()
            tiles_picked = self.get_tiles_from_garbage(choiceColor)
            if tiles_picked is not None:
                break

        while True:
            print("In which line you want to put your(s) " + tiles_picked[0].color + " tile(s) (1 to 5)")
            choiceLine, color = self.validate_chosen_line(tiles_picked)
            result = self.check_line_availability(choiceLine, color, tiles_picked)
            if result: break

        return True



    def is_game_over(self):
        for player in self.players:
            for line in player.board.wall:
                if len(line) == 5:
                    print("End of game.")
                    return True
        return False
    
    def is_turn_over(self):
        if len(self.garbage) == 0 and all(len(display) == 0 for display in self.factory.factory_displays):
            print("End of turn.")
            return True
        return False

    def play_round(self):
        round = 1
        while True:
            if self.is_turn_over():
                for player in self.players:
                    for tile in player.board.broken:
                        if tile.color == 'start':
                            player.starter_tile = tile
                            player.board.broken.remove(tile)
                return True
            print("It's " + str(self.current_player) + " turn. Round " + str(round))
            self.prints.print_starter_tile(self.players, self.current_player)
            print("Choose your action: ")
            print('1 - Buy from factory display')
            print('2 - Buy from garbage')        
            choice = input()
            choice = int(choice)
            if choice == 1:
                result = self.buy_from_factory()
                if result: break
            elif choice == 2:
                result = self.buy_from_garbage()
                if result: break
            else:
                print("Invalid Oprion")
        self.current_player = (self.current_player + 1) % len(self.players)
        round += 1
        return False
