# BlackJack

import random

def deal_card():
    """Returns a random card from the deck!"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes input from cards list and calculates to return the score!"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Compares the score of the dealer and the user to return a winner"""
    if c_score == u_score:
        return "it's a draw"
    elif u_score == 0:
        return "You won with a Blackjack"
    elif c_score == 0:
        return "You lose, Dealer has a Blackjack"
    elif u_score > 21:
        return "Your score is over 21, You lose!"
    elif c_score > 21:
        return "Dealer score is over 21, You win"
    elif u_score > c_score:
        return "Your score is higher, You win"
    else:
        return "You lose"

def play_game():
    computer_cards = []
    user_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)

        print(f"Your cards are {user_cards} and your score is {user_score}.")
        print(f"Computer's first card is {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to continue or type 'n' to end game!: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final deck is {user_cards} and your score is {user_score}")
    print(f"The Dealer's deck is {computer_cards} and the score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play Blackjack?, type 'y for yes and 'n' for no': ") == "y":
    print("\n" * 20)
    play_game()