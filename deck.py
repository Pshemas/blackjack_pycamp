from constants import SuitsRanks
from card import Card
from random import shuffle


class Deck:
    """stores a shuffled deck of cards"""

    def __init__(self) -> None:
        self.cards = []
        self.prepare_new_deck()

    def prepare_new_deck(self):
        self.cards = [
            Card(suit, rank)
            for rank in SuitsRanks().generate_ranks()
            for suit in SuitsRanks().generate_suits()
        ]
        shuffle(self.cards)
