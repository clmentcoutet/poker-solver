from typing import List

from src.Board import Board
from src.Deck import Deck
from src.Hand import Hand
from src.Player import Player
from src.Pot import Pot


class Round:
    def __init__(
        self,
        players: List[Player],
        deck: Deck,
        small_blind: int,
        big_blind: int,
        dealer: Player,
    ):
        self.players = players
        self.deck = deck
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.dealer = dealer
        self.board: Board = Board()
        self.pot: Pot = Pot()

    def __repr__(self):
        return f"Round: {self.players}, small blind: {self.small_blind}, big blind: {self.big_blind}"

    def play(self):
        # deal 2 cards to each player starting for the player to the left of the dealer
        players = self.players[self.players.index(self.dealer) + 1 :] + self.players[
            : self.players.index(self.dealer)
        ]
        for player in self.players:
            player.add_hand(Hand(self.deck.deal(2)))