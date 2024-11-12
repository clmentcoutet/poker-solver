from src.Card import Card


class Hand:
    def __init__(self, cards: list[Card], hand_size: int = 2):
        if len(cards) != hand_size:
            raise ValueError(f"Hand must have {hand_size} cards")
        self.cards = cards

    def __repr__(self):
        return str(self.cards)
