from logo import logo
import random
import os

def deal_card():
    """Return the random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6 , 7, 8 ,9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, com_score):
    if user_score == com_score:
        return "Draw"
    elif com_score == 0:
        return "Lose, opponent has BlackJack"
    elif user_score == 0:
        return "you Win with BlackJack"
    elif user_score > 21:
        return "Busted!!, You lose"
    elif com_score > 21:
        return "Opponent busted!!, You win"
    elif user_score > com_score:
        return "You win!!"
    else:
        return "You lose!!"

def play_game():
    print(logo)
    user_card = []
    com_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        com_card.append(deal_card())

    while  not is_game_over:
        user_score = calculate_score(user_card)
        com_score = calculate_score(com_card)
        print(f" Your cards: {user_card}, current score: {user_score}")
        print(f" Computer's cards: {com_card[0]}")

        if user_score == 0 or com_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while com_score != 0 and com_score < 17:
        com_card.append(deal_card())
        com_score = calculate_score(com_card)

    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {com_card}, final score: {com_score}")
    print(compare(user_score, com_score))

while input("Do you wanna play another game? typr 'y' or 'n': ").lower() == 'y':
    os.system('cls')
    play_game()