from players import Player
from deck import Deck
from constants import BlackjackCardScoring


class BlackjackGame:
    """blueprint for the game and helper methods"""

    def __init__(self) -> None:
        self.players = []
        self.dealer = Player("dealer")
        self.deck = Deck()

    @staticmethod
    def calculate_handvalue(player: Player) -> None:
        """Calculates total for cards in players hand and puts that value
        in handvalue of a given player"""
        total = 0
        for card in player.hand:
            total += card.value
        if len(player.hand) <= 2:
            counter = 0
            for card in player.hand:
                if card.rank == "Ace":
                    total += 10 - counter
                    counter += 1
        player.handvalue = total

    @staticmethod
    def is_not_over21(player: Player) -> bool:
        """check whether player's handvalue has not exceeded 21"""
        isbelow21 = True
        if player.handvalue > 21:
            isbelow21 = False
        return isbelow21

    def assign_card_values(self):
        for card in self.deck.cards:
            card.value = BlackjackCardScoring().values[card.rank]

    def initialdraw(self):
        """adds 2 cards to players hands, including dealer"""
        for player in self.players:
            for _ in range(2):
                player.hand.append(self.deck.cards.pop())
        for _ in range(2):
            self.dealer.hand.append(self.deck.cards.pop())

    def clear_hands(self):
        """empties players and dealer's hand"""
        for player in self.players:
            player.clear_hand()
        self.dealer.clear_hand()

    def players_turn(self):
        """player turn loop"""
        for player in self.players:
            self.calculate_handvalue(player)
            print(player)
            while self.is_not_over21(player):
                picknewcard = input("Dobierasz t/n? ")
                if picknewcard == "n":
                    break
                elif picknewcard == "t":
                    player.hand.append(self.deck.cards.pop())
                    self.calculate_handvalue(player)
                    print(player)
                else:
                    print("Wprowadzono nieprawidłową wartość.")

    def dealer_turn(self, top_player_handvalue: int):
        """dealer turn loop"""
        self.calculate_handvalue(self.dealer)
        while self.dealer.handvalue < top_player_handvalue:
            self.dealer.hand.append(self.deck.cards.pop())
            self.calculate_handvalue(self.dealer)
        print(self.dealer)
