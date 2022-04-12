from dataclasses import dataclass, field


@dataclass(frozen=True)
class SuitsRanks:
    """Container class to generate signs and ranks used in most popular card deck type"""

    suits: tuple = field(
        default_factory=lambda: ("Clubs", "Diamonds", "Hearts", "Spades")
    )
    ranks: tuple = field(
        default_factory=lambda: (
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        )
    )

    def generate_suits(self):
        for suit in self.suits:
            yield suit

    def generate_ranks(self):
        for rank in self.ranks:
            yield rank


@dataclass(frozen=True)
class BlackjackCardScoring:
    """Container for card values used in BlackJack game."""

    values: dict = field(
        default_factory=lambda: {
            "Ace": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
        }
    )
