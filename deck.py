from constants import SuitsRanks
from card import Card
from random import shuffle


class Deck:
    """stores a shuffled deck of cards"""

    def __init__(self) -> None:
        self.currentdeck = []
        self.add_all_cards_shuffled()

    def add_all_cards_shuffled(self):
        self.currentdeck += [
            Card(suit, rank)
            for rank in SuitsRanks().generate_ranks()
            for suit in SuitsRanks().generate_suits()
        ]
        shuffle(self.currentdeck)
