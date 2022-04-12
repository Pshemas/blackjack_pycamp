from players import Player
from blackjack_game import BlackjackGame


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
