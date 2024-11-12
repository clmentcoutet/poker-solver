from typing import Optional

from typing import List
from src import constants

from src.Deck import Deck
from src.Player import Player
from src.Round import Round
from src.Stack import Stack


class Game:
    def __init__(
            self,
            players: List[Player],
            deck: Optional[Deck] = None,
    ):
        if len(players) < 2:
            raise ValueError("Game must have at least 2 players")
        self.players: List[Player] = players
        self.deck: Deck = (
            deck if deck is not None else Deck(constants.CARDS, constants.SUITS)
        )
        self.rounds: List[Round] = []
        self.current_dealer = None
        self.small_blind = None
        self.big_blind = None

    def __repr__(self):
        return f"Game: {self.players}, small blind: {self.small_blind}, big blind: {self.big_blind}"

    def init_game(self, small_blind: int, big_blind: int, base_stack: Stack):
        """
        Initialize the game with the blinds and stack.

        Parameters
        ----------
        small_blind : int
            the small blind amount
        big_blind : int
            the big blind amount
        base_stack : Stack
            the starting stack for each player
        """
        for player in self.players:
            player.stack = base_stack
        self.current_dealer = self.players[0]
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.rounds.append(
            Round(
                self.players,
                self.deck,
                self.small_blind,
                self.big_blind,
                self.current_dealer,
            )
        )

    def play(self):
        """
        Play the game.
        """
        while True:
            round = self.rounds[-1]
            winner = round.play()
            self.current_dealer = self.players[
                (self.players.index(self.current_dealer) + 1) % len(self.players)
                ]
            self.players = [
                player for player in self.players if player.stack.total > 0
            ]
            if len(self.players) == 1:
                return self.players[0]
            if len(self.players) == 0:
                return None
            self.rounds.append(
                Round(
                    self.players,
                    self.deck,
                    self.small_blind,
                    self.big_blind,
                    self.current_dealer,
                )
            )
