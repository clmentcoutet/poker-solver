class Chip:
    def __init__(self, price: int):
        self.price: int = price

    def __repr__(self):
        return f"Chip price: {self.price}"

    def __str__(self):
        return f"Chip price: {self.price}"

    @property
    def value(self):
        return self.price
