""" Program to play Blackjack

written by K. Gray, March 2023
"""
import random
new_deck = [("two", "hearts"), ("three", "hearts"),
            ("four", "hearts"), ("five", "hearts"), ("six", "hearts"),
            ("seven", "hearts"), ("eight", "hearts"), ("nine", "hearts"),
            ("ten", "hearts"), ("jack", "hearts"), ("queen", "hearts"),
            ("king", "hearts"), ("ace", "hearts"),
            ("two", "diamonds"), ("three", "diamonds"),
            ("four", "diamonds"), ("five", "diamonds"), ("six", "diamonds"),
            ("seven", "diamonds"), ("eight", "diamonds"), ("nine", "diamonds"),
            ("ten", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"),
            ("king", "diamonds"), ("ace", "diamonds"),
            ("two", "clubs"), ("three", "clubs"),
            ("four", "clubs"), ("five", "clubs"), ("six", "clubs"),
            ("seven", "clubs"), ("eight", "clubs"), ("nine", "clubs"),
            ("ten", "clubs"), ("jack", "clubs"), ("queen", "clubs"),
            ("king", "clubs"), ("ace", "clubs"),
            ("two", "spades"), ("three", "spades"),
            ("four", "spades"), ("five", "spades"), ("six", "spades"),
            ("seven", "spades"), ("eight", "spades"), ("nine", "spades"),
            ("ten", "spades"), ("jack", "spades"), ("queen", "spades"),
            ("king", "spades"), ("ace", "spades"),
            ]
card_values = {"two": 2, "three": 3,
               "four": 4, "five": 5, "six": 6,
               "seven": 7, "eight": 8, "nine": 9,
               "ten": 10, "jack": 10, "queen": 10,
               "king": 10, "ace": 1}


def score_hand(hand):
    """Calculate the score value of a hand of cards"""

    score = 0
    for score_card in hand:
        score += card_values[score_card[0]]
    for score_card in hand:
        if score < 12:
            if score_card[0] == "ace":
                score += 10
    return score


def draw_card():
    """Pull a random card from the deck"""

    size = len(card_deck)
    new_card = card_deck.pop(random.randrange(0, size,))
    return new_card


def get_user_response(prompt, valid_responses):
    """Get and validate a single character response from a user"""

    user_response = ''
    while user_response not in valid_responses:
        try:
            user_response = input(prompt)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt Error")
            pass
        if user_response:
            user_response = user_response[0].lower()
        if user_response not in valid_responses:
            print("I don't understand that reply.")
            print(f'Valid responses are {valid_responses}')
    return user_response


dealer_wins = 0
player_wins = 0
print("Welcome to Blackjack")
play_again = 'y'
while play_again == 'y':
    player_hand = []
    dealer_hand = []
    card_deck = new_deck
    print(f'{"":*^50}')
    dealer_hand.append(draw_card())
    card = draw_card()
    print(f'The dealer draws a hidden card and the {card[0]} of {card[1]}')
    dealer_hand.append(card)
    dealer_score = score_hand(dealer_hand)
    card = draw_card()
    print(f'You draw the {card[0]} of {card[1]} and', end=" ")
    player_hand.append(card)
    card = draw_card()
    print(f'the {card[0]} of {card[1]}.')
    player_hand.append(card)
    player_score = score_hand(player_hand)
    print(f'Your total is {player_score}')
    try:
        response = get_user_response("Do you wish to Hit or Stand?(h/s)", ('h', 's'))
    except Exception as error:
        print(f'\n{type(error).__name__} occurred.')
        print('Thank you for playing')
        exit()
    while response == 'h':
        card = draw_card()
        player_hand.append(card)
        print(f'You drew the {card[0]} of {card[1]}')
        player_score = score_hand(player_hand)
        print(f'your score is {player_score}')
        if player_score > 20:
            break
        try:
            response = get_user_response("Do you wish to Hit or Stand?(h/s)", ('h', 's'))
        except Exception as error:
            print(f'\n{type(error).__name__} occurred.')
            print('Thank you for playing')
            exit()
    hole_card = dealer_hand[0]
    print(f"The dealer reveals the hidden card as the {hole_card[0]} of {hole_card[1]}")
    while dealer_score < 17 and player_score < 22:
        card = draw_card()
        dealer_hand.append(card)
        print(f'The dealer draws the {card[0]} of {card[1]}')
        dealer_score = score_hand(dealer_hand)
        if dealer_score > 21:
            break
    print(f'Your total {player_score}')
    print(f'Dealer total {dealer_score}')
    if player_score > 21:
        print('You have busted! The dealer wins')
        dealer_wins += 1
    elif dealer_score > 21:
        print('The dealer has busted! You win!')
        player_wins += 1
    else:
        if dealer_score < player_score:
            print('You have won!')
            player_wins += 1
        else:
            print('The dealer has won!')
            dealer_wins += 1
    print(f'You have won {player_wins} games')
    print(f'The dealer has won {dealer_wins} games')
    try:
        play_again = get_user_response('Do you wish to play again?', ('y', 'n'))
    except Exception as error:
        print(f'\n{type(error).__name__} occurred.')
        print('Thank you for playing')
        exit()
print("Thank you for playing")
print("Please feel free to come back again")
