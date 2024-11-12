from src.Game import Game
from src.Player import Player
from src.Stack import DEFAULT_STACK

if __name__ == "__main__":
    player_1 = Player("Player 1")
    player_2 = Player("Player 2")
    player_3 = Player("Player 3")
    player_4 = Player("Player 4")

    game = Game([player_1, player_2, player_3, player_4])
    game.init_game(10, 20, DEFAULT_STACK)

    game.play()
