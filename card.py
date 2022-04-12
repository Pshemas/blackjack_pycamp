from constants import BlackjackCardScoring

# @TODO: wywalic value i przeniesc do BlackJack Game -
# bo punktacja zalezy od rodzaju gry (grajac w np. makao bylaby inna)


class Card:
    """single card representation."""

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank
        self.value = BlackjackCardScoring().values[self.rank]

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"
