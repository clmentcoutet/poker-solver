from typing import Dict, List

from typing import Optional

from src.Hand import Hand
from src.Stack import Stack
from src.custom_typing import RoundName


class Player:
    """
    A class to represent a player in the game.

    Attributes
    ----------
    name : str
        the name of the player
    hand : Hand
        the player's hand
    stack : Stack
        the player's stack of chips
    bet : Stack
        the player's bet in the current round
    """

    def __init__(self, name: str):
        self.name = name
        self.hand: Optional[Hand] = None
        self.stack: Stack = Stack()
        self.bet: Dict[RoundName, List[Stack]] = {
            round_name: [] for round_name in RoundName
        }

    def __str__(self):
        return f"Player: {self.name} - Stack: {self.stack}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self is other

    def add_hand(self, hand: Hand):
        self.hand = hand

    def init_stack(self, stack: Stack):
        self.stack = stack

    def reset(self):
        self.hand = None
        self.stack = Stack()

    def bet_chip(self, quantity: int, current_round: RoundName):
        if current_round not in self.bet:
            raise ValueError(f"Invalid round: {current_round}")

        self.stack.remove_chip(quantity)
        self.bet[current_round].append(Stack(quantity))
