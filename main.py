from players import Player
from blackjack_game import BlackjackGame


def Blackjack_singleplayer_gameloop():
    """a simpliefied blackjack game loop for a single player"""
    player1 = Player(input("Imie gracza: "))
    game = BlackjackGame()
    game.players.append(player1)
    game.assign_card_values()

    while True:
        game.blackjack_singleplayer_gameloop()

        playagain = input("Kolejne rozdanie t/n? ")
        while playagain not in {"t", "n"}:
            print("Zła wartość!")
            playagain = input("Kolejne rozdanie t/n? ")

        if playagain == "n":
            print("Koniec gry!")
            print("Wyniki:")
            for player in game.players:
                print(f"{player.name}: {player.score}")
            print(f"Krupier: {game.dealer.score}")
            break

        else:
            # currently new deck is used during each play
            game.deck.prepare_new_deck()
            game.assign_card_values()
            game.clear_hands()


if __name__ == "__main__":
    Blackjack_singleplayer_gameloop()
