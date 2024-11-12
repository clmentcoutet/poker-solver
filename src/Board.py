from typing import List, Optional

from src.Card import Card


class Board:
    def __init__(self):
        self.flop: Optional[List[Card]] = None
        self.turn: Optional[Card] = None
        self.river: Optional[Card] = None

    @property
    def cards(self):
        return self.flop + [self.turn, self.river]

    def __repr__(self):
        return str(self.cards)

    def deal_flop(self, cards: List[Card]):
        if len(cards) != 3:
            raise ValueError("Flop must have 3 cards")
        self.flop = cards

    def deal_turn(self, card: Card):
        self.turn = card

    def deal_river(self, card: Card):
        self.river = card

    def reset(self):
        self.flop = None
        self.turn = None
        self.river = None
