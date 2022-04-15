from card import Card


def test_card_repr():
    """check whether repr of the card is constructed correctly"""
    rank = "costam"
    suit = "costam"
    samplecard = Card(suit, rank)
    assert samplecard.__repr__() == f"{rank} of {suit}"
