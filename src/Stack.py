from typing import List

from typing import Dict, Optional

from src.Chip import Chip


class Stack:
    """
    A class to represent a stack of chips.

    Attributes
    ----------
    stack : Dict[Chip, int]
        a dictionary of chips and their quantities
    """

    def __init__(self, quantity: Optional[int] = None, chips: Optional[List[Chip]] = None):
        self.stack: Dict[Chip, int] = {}
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity must be greater than or equal to 0")
            if quantity > 0:
                if chips is None:
                    self.add_chip(quantity)
                else:
                    for chip in chips:
                        self.add_chip(quantity, chip)


    def __repr__(self):
        return str(self.stack)

    @property
    def total(self):
        """
        Calculate the total value of the stack.

        Returns
        -------
        int
            the total value of the stack
        """
        return sum([chip.value * quantity for chip, quantity in self.stack.items()])

    def add_chip(self, quantity: int, chip: Optional[Chip] = None):
        """
        Add a chip to the stack.

        Parameters
        ----------
        chip : Chip
            the chip to add
        quantity : int
            the quantity of chips to add
        """
        # if chip is not provided, add the highest value chip available until the quantity is reached
        if chip is None:
            for chip in sorted(self.stack.keys(), key=lambda x: x.value, reverse=True):
                if quantity == 0:
                    break
                if chip in self.stack:
                    self.stack[chip] += quantity
                else:
                    self.stack[chip] = quantity
                quantity = 0
        else:
            if chip in self.stack:
                self.stack[chip] += quantity
            else:
                self.stack[chip] = quantity

    def remove_chip(self, quantity: int, chip: Optional[Chip] = None):
        """
        Remove a chip from the stack.
        :param chip:
        :param quantity:
        :return:
        """
        # if chip is not provided, remove the highest value chip available until the quantity is reached
        if chip is None:
            for chip in sorted(self.stack.keys(), key=lambda x: x.value, reverse=True):
                if quantity == 0:
                    break
                if self.stack[chip] > quantity:
                    self.stack[chip] -= quantity
                    break
                quantity -= self.stack[chip]
                self.stack[chip] = 0
        else:
            if chip not in self.stack:
                raise ValueError(f"Chip {chip} not in stack")
            if self.stack[chip] < quantity:
                raise ValueError(f"Chip {chip} quantity is less than {quantity}")
            self.stack[chip] -= quantity

    def clear(self):
        """
        Clear the stack.
        """
        self.stack = {}


DEFAULT_STACK = Stack(10, [Chip(1), Chip(5), Chip(25), Chip(100), Chip(500)])