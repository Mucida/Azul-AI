from azul.game import AzulGame

if __name__ == "__main__":
    num_players = 2  # Set the number of players
    game = AzulGame(num_players)
    
    while not game.is_game_over():
        game.play_round()
        game.current_player = (game.current_player + 1) % len(game.players)
        game.round += 1


'''
corrigir parece qo player 1 sempre coloca o STARTER no garbage

corrigir quando jogador 1 volta a jogar e escolhe colocar na linha uma cor diferente da q ja tem la, ele da o aviso mas prossegue para o jogador 2
'''