from azul.game import AzulGame

if __name__ == "__main__":
    num_players = 2  # Set the number of players
    game = AzulGame(num_players)
    
    while not game.is_game_over():
        while not game.is_turn_over():
            result = game.play_round()
        


'''
corrigir quando jogador 1 volta a jogar e escolhe colocar na linha uma cor diferente da q ja tem la, ele da o aviso mas prossegue para o jogador 2
'''