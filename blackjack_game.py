from players import Player
from deck import Deck


class BlackjackGame:
    """blueprint for the game and helper methods"""

    def __init__(self) -> None:
        self.players = []
        self.dealer = Player("dealer")
        self.deck = Deck()

    def initialdraw(self):
        for player in self.players:
            for _ in range(2):
                player.hand.append(self.deck.currentdeck.pop())
        for _ in range(2):
            self.dealer.hand.append(self.deck.currentdeck.pop())

    def check_initial_wincondition(self) -> bool:
        won = False
        for player in self.players:
            if player.handvalue == 21:
                player.score += 1
                won = True
        return won

    def isover21(self) -> bool:
        isover = False
        for player in self.players:
            if player.handvalue > 21:
                isover = True
        return isover

    def calculate_handvalue(self, player: Player) -> None:
        total = 0
        for card in player.hand:
            total += card.value
        if len(player.hand) <= 2:
            counter = 0
            for card in player.hand:
                if card.rank == "Ace":
                    total += 10 - counter
                    counter += 1
        self.total = total

    def dealerplay(self, top_player_handvalue: int, game):
        while self.dealer.handvalue < top_player_handvalue:
            self.dealer.hand.append(game.deck.currentdeck.pop())
            self.calculate_handvalue(self.dealer)
