# @TODO: liczenie pkt jako element klasy Blackjack Game - bo inna gra bedzie miala inna punktacje


class Hand:
    """stores cards player has in hand and has method to calculate its value"""

    def __init__(self) -> None:
        self.cards = []
        self.total = 0
        self.calculate_total()

    def calculate_total(self) -> None:
        total = 0
        for card in self.cards:
            total += card.value
        if len(self.cards) <= 2:
            counter = 0
            for card in self.cards:
                if card.rank == "Ace":
                    total += 10 - counter
                    counter += 1
        self.total = total
