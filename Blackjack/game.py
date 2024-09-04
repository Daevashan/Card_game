import random

#deck of cards/dealer/player hands
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6,
        7, 8, 9, 10, "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K"]
player = []
dealer = []


#deal card
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


#hand total
def totalHand(turn):
    total = 0
    faceCard = ["J", "Q", "K"]
    ace_count = 0

    for card in turn:
        if card in range(2, 11):
            total += card
        elif card in faceCard:
            total += 10
        elif card == "A":
            ace_count += 1
            total += 11  # Count each Ace as 11 initially

            # Adjust for Aces if the total exceeds 21
    while total > 21 and ace_count > 0:
        total -= 10  # Convert one Ace from 11 to 1
        ace_count -= 1
    return total


#determine winner
def revealDealerCards():
    if len(dealer) == 2:
        return dealer[0]
    elif len(dealer) > 2:
        return dealer[0], dealer[1]


def playersTurn():
    # player's turn
    while True:
        print(f"Your hand is {player} with total of {totalHand(player)}")

        if (totalHand(player) == 21) and (len(player) == 2):
            print("You got blackjack, you Won!")
            return True

        print(f"Dealer's hand is: {revealDealerCards()} and X.")
        playerTurn = input("Select: \n1.Hit \n2.Stay \n")
        if playerTurn == "1":
            dealCard(player)
            print("You hit.")
            if totalHand(player) > 21:
                print(f"Your hand is {player} with total of {totalHand(player)} so you Bust! \nYou lost.")
                return True
            else:
                continue
        else:
            return False


def dealersTurn():
    # print(f"Dealer's cards are {dealer[0], dealer[1]}")

    #dealer's turn
    while True:
        print(f"Dealer's hand is {dealer} and count is {totalHand(dealer)}.")

        if totalHand(dealer) > 21 and totalHand(player) < 22:
            print(f"Dealer bust!\nYou Won.")
            break
        elif totalHand(dealer) < 17 and totalHand(player) < 22:
            dealCard(dealer)
            print("Dealer hit.")
            continue
        elif totalHand(dealer) > totalHand(player) < 22:
            print(f"You lost.")
            break
        elif totalHand(dealer) < totalHand(player) < 22:
            print(f"You Won.")
            break
        elif totalHand(dealer) == totalHand(player) < 22:
            print(f"You pushed.")
            break
        else:
            print(f"You lost.")
            break


#game loop
def gameLoop():
    while True:
        for i in range(2):
            dealCard(player)
            dealCard(dealer)

        gameEnded = playersTurn()

        if not gameEnded:
            dealersTurn()

        gameContinue = input("Want to play again? (y/n): \n")
        if gameContinue == "y":
            player.clear()
            dealer.clear()
            continue
        break
    print("Game over.")


gameLoop()
