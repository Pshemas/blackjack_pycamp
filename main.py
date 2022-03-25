from random import shuffle
from constants import VALUE


class SuitsRanks:
    """Container class with the signs and ranks used in most popular card deck type"""

    @staticmethod
    def generate_suits():
        suits = {"Clubs", "Diamonds", "Hearts", "Spades"}
        for suit in suits:
            yield suit

    @staticmethod
    def generate_ranks():
        ranks = {
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        }
        for rank in ranks:
            yield rank


class BlackjackCardValues:
    """Container for card values used in BlackJack game."""

    def __init__(self) -> None:
        self.values = {
            "Ace": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
        }


class Card:
    """single card representation."""

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank
        self.value = VALUE[self.rank]

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    """stores a shuffled deck of cards"""

    def __init__(self) -> None:
        self.currentdeck = []
        self.add_all_cards_shuffled()

    def add_all_cards_shuffled(self):
        self.currentdeck += [
            Card(suit, rank)
            for rank in SuitsRanks.generate_ranks()
            for suit in SuitsRanks.generate_suits()
        ]
        shuffle(self.currentdeck)


class Hand:
    """stores cards player has in hand and has method to calculate its value"""

    def __init__(self) -> None:
        self.cards = []
        self.total = 0
        self.calculate_total()

    def calculate_total(self) -> None:
        total = 0
        for card in self.cards:
            total += card.value
        if len(self.cards) <= 2:
            counter = 0
            for card in self.cards:
                if card.rank == "Ace":
                    total += 10 - counter
                    counter += 1
        self.total = total


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


def main():
    player1 = Player(input("Imie gracza: "))
    game = BlackjackGame()
    game.players.append(player1)
    game.initialdraw()
    # Player Turn
    print(f"Karty gracza {player1.name}:")
    player1.showcards()
    player1.hand.calculate_total()
    print(f"Wynik: {player1.hand.total}")
    if game.check_initial_wincondition():
        print("Oczko! Następne rozdanie.")
    else:
        while True:
            picknewcard = input("Dobierasz t/n ? ")
            if picknewcard == "n":
                break
            player1.hand.cards.append(game.deck.currentdeck.pop())
            player1.showcards()
            player1.hand.calculate_total()
            print(f"Wynik: {player1.hand.total}")
            if game.isover21():
                break

        if game.isover21():
            game.dealer.score += 1
            print("masz ponad 21. Krupier wygrywa.")
        else:
            game.dealer.dealerplay(player1.hand.total, game)

        if game.dealer.hand.total <= 21:
            game.dealer.score += 1
            print("Krupier wygrał!")
        else:
            player1.score += 1
            print("Wygrałeś!")

        print(f"Dealer miał:")
        game.dealer.showcards()


if __name__ == "__main__":
    main()
