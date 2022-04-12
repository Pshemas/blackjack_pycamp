from hand import Hand

# @TODO: ustawic hand jako atrybut gracza


class Player:
    """Contains player data"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = Hand()
        self.score = 0

    def showcards(self):
        for card in self.hand.cards:
            print(card)


class BlackjackDealer(Player):
    """extends player class to add logic for the dealer."""

    def __init__(self):
        super().__init__("dealer")

    def dealerplay(self, top_player_handtotal: int, game):
        while self.hand.total < top_player_handtotal:
            self.hand.cards.append(game.deck.currentdeck.pop())
            self.hand.calculate_total()
