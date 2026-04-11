import random

# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Deck class
class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


# Function to display hand
def display_hand(hand):
    print("\nYour hand:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")


# Function to replace selected cards
def replace_cards(hand, deck, indices):
    for i in indices:
        if 0 <= i < len(hand):
            hand[i] = deck.deal()


# Main game function
def play_poker():
    deck = Deck()

    # Deal 5 cards
    hand = [deck.deal() for _ in range(5)]
    display_hand(hand)

    # Ask For which cards to replace
    user_input = input("\nEnter card positions to replace (e.g., 1,3,5) or press Enter to keep all: ")

    if user_input.strip() != "":
        try:
            indices = [int(x.strip()) - 1 for x in user_input.split(",")]
            replace_cards(hand, deck, indices)
        except ValueError:
            print("Invalid input. No cards replaced.")

    # Dispay the final hand
    display_hand(hand)


# Call the game
if __name__ == "__main__":
    play_poker()