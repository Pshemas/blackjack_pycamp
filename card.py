class Card:
    """single card representation."""

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank
        self.value = 0

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"
