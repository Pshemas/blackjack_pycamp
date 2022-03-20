from random import shuffle
from constants import VALUE


class SuitsRanks:
    @staticmethod
    def generate_suits():
        suits = {"Clubs", "Diamonds", "Hearts", "Spades"}
        for suit in suits:
            yield suit

    @staticmethod
    def generate_ranks():
        ranks = {
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
        }
        for rank in ranks:
            yield rank


class BlackjackCardValues:
    def __init__(self) -> None:
        self.values = {
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


class Card:
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank
        self.value = VALUE[self.rank]

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self) -> None:
        self.currentdeck = []

    def add_all_cards_shuffled(self):
        self.currentdeck += [
            Card(suit, rank)
            for rank in SuitsRanks.generate_ranks()
            for suit in SuitsRanks.generate_suits()
        ]
        shuffle(self.currentdeck)
        # for suit in SUITS:
        #     for rank in RANKS:
        #         self.currentdeck.append(Card(rank, suit))


class Hand:
    def __init__(self) -> None:
        self.cards = []
        self.total = self.calculate_total()

    def calculate_total(self) -> None:
        total = 0
        for card in self.cards:
            total += card.value
        if len(self.cards) <= 2:
            counter = 0
            for card in self.cards:
                print(card.value)
                if card.rank == "Ace":
                    print(counter)
                    total += 10 - counter
                    counter += 1
        self.total = total


class Player:
    def __init__(self) -> None:
        self.hand = Hand()
        self.score = 0


class BlackjackDealer:
    def __init__(self) -> None:
        self.hand = Hand()
        self.score = 0


def main():
    mydeck = Deck()
    mydeck.add_all_cards_shuffled()
    print(mydeck.currentdeck)
    print(len(mydeck.currentdeck))


if __name__ == "__main__":
    main()
