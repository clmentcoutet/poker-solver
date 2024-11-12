from typing import Dict

from src.Chip import Chip
from src.Stack import Stack


class Pot(Stack):
    """
    A class to represent the pot of chips, similar to a stack of chips.
    but with the addition of side pots.

    Attributes
    ----------
    super().stack : Dict[Chip, int]
        a dictionary of chips and their quantities
    side_pots : Dict[int, Dict[Chip, int]]
        a dictionary of side pots and their chips and quantities
        with the key being the player id
    """

    def __init__(self):
        super().__init__()
        self.side_pots: Dict[int, Dict[Chip, int]] = {}
