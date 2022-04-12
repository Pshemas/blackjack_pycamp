from players import BlackjackDealer
from deck import Deck


class BlackjackGame:
    """blueprint for the game and helper methods"""

    def __init__(self) -> None:
        self.players = []
        self.dealer = BlackjackDealer()
        self.deck = Deck()

    def initialdraw(self):
        for player in self.players:
            for _ in range(2):
                player.hand.cards.append(self.deck.currentdeck.pop())
        for _ in range(2):
            self.dealer.hand.cards.append(self.deck.currentdeck.pop())

    def check_initial_wincondition(self) -> bool:
        won = False
        for player in self.players:
            if player.hand.total == 21:
                player.score += 1
                won = True
        return won

    def isover21(self) -> bool:
        isover = False
        for player in self.players:
            if player.hand.total > 21:
                isover = True
        return isover
