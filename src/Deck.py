import random
from typing import List

from src.Card import Card


class Deck:
    def __init__(self, cards: list[str], suits: list[str]):
        self.cards = []
        self.fill_deck(cards, suits)

    def __repr__(self):
        return str(self.cards)

    def fill_deck(self, cards: list[str], suits: list[str]):
        for suit in suits:
            for card in cards:
                self.cards.append(Card(suit, card))

    def deal(self, number: int = 1) -> List[Card]:
        dealt_cards = []
        for _ in range(number):
            dealt_cards.append(self.cards.pop())
        return dealt_cards

    def burn_card(self):
        self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
