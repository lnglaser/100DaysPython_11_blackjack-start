############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
# blackjack = 21
player_score = 0
dealer_score = 0
player_blackjack = None
dealer_blackjack = None
# Selects random card from "cards" list and returns it


def deal_card(deck):
    dealt_card = deck[random.randrange(len(deck))]
    return (dealt_card)

# Adds up value of cards in hand and returns the total (replaces 11 with 1 if score is already over 21)


def scoring(hand, score):
    score = sum(hand)
    if score > 21:
        for card in hand:
            if card == 11:
                score -= 10

    return (score)


def card_hit(hand):
    hand.append(deal_card(cards))

# Checks scores against value of 21 to see if score is over, under or exact


def check_blackjack(score):
    blackjack = None
    if score < 21:
        blackjack = "under"
    elif score == 21:
        blackjack = "yes"
    else:
        blackjack = "over"
    return (blackjack)


# Testing hands:
# player_hand = [11, 11]

# Intial deal - 2 cards each to player and dealer
for card in range(2):
    player_hand.append(deal_card(cards))
    dealer_hand.append(deal_card(cards))

player_score = scoring(player_hand, player_score)
dealer_score = scoring(dealer_hand, dealer_score)

print(f"Your hand: {player_hand} - Your current score: {player_score}")
print(f"Dealer's first card: {dealer_hand[0]}")

# Loop to check if player wants to hit or stay, and for dealer to hit until 21 or bust
keep_going = True
while player_score < 21:
    while keep_going == True:
        hit_or_stay = input("Would you like to hit? (y/n): ").lower()
        if hit_or_stay == "y":
            player_hand.append(deal_card(cards))
            if dealer_score < 21:
                dealer_hand.append(deal_card(cards))
                dealer_score = scoring(dealer_hand, dealer_score)
                dealer_blackjack = check_blackjack(dealer_score)
                print(f"Dealer's hand: {dealer_hand} - {dealer_blackjack}")

        # While loop for dealer to take cards if score under 21


# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
