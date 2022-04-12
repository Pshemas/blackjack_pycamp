class Player:
    """Contains player data"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.handvalue = 0
        self.score = 0

    def showcards(self):
        for card in self.hand:
            print(card)
