class Prints:
    
    def print_colored_text_with_square(color, x):
        # ANSI escape code for changing text color
        color_code = {
            'red': '\033[91m',
            'white': '\033[97m',
            'blue': '\033[94m',
            'black': '\033[30m',
            'orange': '\033[93m',
        }

        # Reset the color after the text
        reset_code = '\033[0m'

        # Check if the color is valid
        if color in color_code:
            colored_text = f"{color_code[color]}■{reset_code}"
            if x == 4:
                print(colored_text)
            else:
                print(colored_text + " ", end='')

    def print_colored_square(self, color, actual_size, size):
        # ANSI escape code for changing text color
        color_code = {
            'red': '\033[91m',
            'white': '\033[97m',
            'blue': '\033[94m',
            'black': '\033[30m',
            'orange': '\033[93m',
        }

        # Reset the color after the text
        reset_code = '\033[0m'
        if color == 'start':
            print("X ")
            return
        # Check if the color is valid
        if color in color_code:
            colored_text = f"{color_code[color]}■{reset_code}"
            
            if actual_size < size-1:
                print(colored_text + " ", end='')
            else:
                print(colored_text)

        
    def print_current(self, choice_line, garbage, players, current_player, Factory):
        print("---------------------------------")
        print("printing garbage:")
        for actual_size, g in enumerate(garbage):
            self.print_colored_square(g.color, actual_size, len(garbage))
        print("---------------------------------")
        print("printing player lines: ")
        for l in players[current_player].board.lines:
            for actual_size, s in enumerate(l):
                if s is not None:
                    self.print_colored_square(s.color, actual_size, len(l))
                else:
                    if actual_size < len(l) - 1:
                        print("_ ", end='')
                    else:
                        print("_")
        print("---------------------------------")
        print("printing player broken " + str(choice_line))
        size = len(players[current_player].board.broken)
        for actual_size, b in enumerate(players[current_player].board.broken):
            if b is not None:
                self.print_colored_square(b.color, actual_size, size)
        print("---------------------------------")
        print("printing factories:")
        Factory.print_factories()
        print("---------------------------------")

    def print_garbage(self, garbage):
        if len(garbage) == 0:
            print("_")
        else:
            for actual_size, g in enumerate(garbage):
                self.print_colored_square(g.color, actual_size, len(garbage))

    def print_starter_tile(self, players, current_player):
        if players[current_player].starter_tile is None:
            print("Player " + str(current_player) + " starter pile: empty")
        else: 
            print("Player " + str(current_player) + " starter pile: " + players[current_player].starter_tile.color)