import pytest
from main import Deck, Card, Hand


@pytest.fixture
def add2aces():
    return [Card("Clubs", "Ace"), Card("Diamonds", "Ace")]


@pytest.fixture
def add2aces_and_two(add2aces):
    return add2aces + [Card("Clubs", "2")]


def test_deckcreation():
    decklist = Deck()
    decklist.add_all_cards_shuffled()
    deckset = set(decklist.currentdeck)
    assert len(decklist.currentdeck) == len(deckset)


def test_decklength():
    testdeck = Deck()
    assert len(testdeck.currentdeck) == 52


def test_hand_2acesonly(add2aces):
    myhand = Hand()
    myhand.cards += add2aces
    print(myhand)
    myhand.calculate_total()
    assert myhand.total == 21


def test_hand_2acesandmore(add2aces_and_two):
    myhand = Hand()
    myhand.cards += add2aces_and_two
    myhand.calculate_total()
    assert myhand.total == 4
