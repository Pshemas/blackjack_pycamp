from deck import Deck
from constants import SuitsRanks


def test_decklength():
    """check deck length"""
    sampledeck = Deck()
    assert len(sampledeck.cards) == 52


def test_deckcards_ranks():
    """check whether deck card ranks exist in SuitsRanks"""
    sampledeck = Deck()
    suits_and_ranks = SuitsRanks()
    for card in sampledeck.cards:
        assert card.rank in suits_and_ranks.ranks


def test_deckcards_suits():
    """check whether deck card suits exist in SuitsRank"""
    sampledeck = Deck()
    suits_and_ranks = SuitsRanks()
    for card in sampledeck.cards:
        assert card.suit in suits_and_ranks.suits


def test_suits_amount():
    """checks whether new deck suits amount is correct"""
    sampledeck = Deck()
    suits = set()
    for card in sampledeck.cards:
        suits.add(card.suit)
    assert len(suits) == 4


def test_ranks_amount():
    """checks whether new deck ranks amount is correct"""
    sampledeck = Deck()
    ranks = set()
    for card in sampledeck.cards:
        ranks.add(card.rank)
    assert len(ranks) == 13
