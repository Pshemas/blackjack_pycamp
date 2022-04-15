from blackjack_game import BlackjackGame


def test_card_values_notzero_after_assignment():
    """tests whether each card gets value assigned"""
    samplegame = BlackjackGame()
    samplegame.assign_card_values()
    for card in samplegame.deck.cards:
        assert card.value != 0


def test_card_values_total_after_assignment():
    """test whether total deck value is correct"""
    samplegame = BlackjackGame()
    samplegame.assign_card_values()
    total = 0
    for card in samplegame.deck.cards:
        total += card.value
    assert total == (40 * 3 + sum(range(1, 11)) * 4)


def test_dealerhandvalue_2aces():
    """test whether the hand value is counted correctly when 2 aces on hand"""
    samplegame = BlackjackGame()
    samplegame.assign_card_values()
    indexes = []
    for _ in range(2):
        for card in samplegame.deck.cards:
            if card.rank == "Ace":
                indexes.append(samplegame.deck.cards.index(card))
                break
    for index in indexes:
        samplegame.dealer.hand.append(samplegame.deck.cards[index])
    samplegame.calculate_handvalue(samplegame.dealer)
    assert samplegame.dealer.handvalue == 21


def test_dealerhandvalue_2kings():
    """test whether the hand value is counted correctly when 2 kings on hand"""
    samplegame = BlackjackGame()
    samplegame.assign_card_values()
    indexes = []
    for _ in range(2):
        for card in samplegame.deck.cards:
            if card.rank == "King":
                indexes.append(samplegame.deck.cards.index(card))
                break
    for index in indexes:
        samplegame.dealer.hand.append(samplegame.deck.cards[index])
    samplegame.calculate_handvalue(samplegame.dealer)
    assert samplegame.dealer.handvalue == 20
