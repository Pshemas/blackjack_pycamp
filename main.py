from players import Player
from blackjack_game import BlackjackGame


def Blackjack_singleplayer_gameloop():
    """a simpliefied blackjack game loop for a single player"""
    player1 = Player(input("Imie gracza: "))
    game = BlackjackGame()
    game.players.append(player1)
    game.assign_card_values()

    while True:
        game.initialdraw()
        game.players_turn()
        if player1.handvalue > 21:
            print("Krupier wygrał! Masz więcej niż 21.")
            print(player1)
            game.dealer.score += 1
        else:
            game.dealer_turn(player1.handvalue)
            if game.dealer.handvalue > 21:
                print("Wygrałeś! Krupier ma ponad 21.")
                player1.score += 1
            else:
                if player1.handvalue > game.dealer.handvalue:
                    print("Wygrałeś! Masz więcej niż krupier.")
                    player1.score += 1
                elif player1.handvalue == game.dealer.handvalue:
                    print("Remis!")
                else:
                    print("Krupier wygrał!")
                    game.dealer.score += 1

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
            game.deck.prepare_new_deck()
            game.assign_card_values()
            game.clear_hands()


if __name__ == "__main__":
    Blackjack_singleplayer_gameloop()
