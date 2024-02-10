import numpy as np

class UpwardPile:
    def __init__(self):
        self.name = 'UpwardPile'
        self.top_card = 1
        self.played_cards = []
    
    def play_card(self, card):
        # If the card is greater than the top card or exactly ten smaller than the top card, play the card
        if card > self.top_card or card == self.top_card - 10:
            self.top_card = card
            self.played_cards.append(card)
            return True
    
    def check_card(self, card):
        # If the card is greater than the top card or exactly ten smaller than the top card, return True
        if card > self.top_card or card == self.top_card - 10:
            return True
        else:
            return False

class DownwardPile:
    def __init__(self):
        self.name = 'DownwardPile'
        self.top_card = 100
        self.played_cards = []
    
    def play_card(self, card):
        # If the card is smaller than the top card or exactly ten greater than the top card, play the card
        if card < self.top_card or card == self.top_card + 10:
            self.top_card = card
            self.played_cards.append(card)
            return True
    
    def check_card(self, card):
        # If the card is smaller than the top card or exactly ten greater than the top card, return True
        if card < self.top_card or card == self.top_card + 10:
            return True
        else:
            return False

class Hand:
    def __init__(self, max_cards) -> None:
        self.cards = np.array([])
        self.max_cards = max_cards

class Deck:
    def deal_cards(self):
        # If the hand size is smaller than 6 fill up to the hand max size
        if len(self.hand.cards) < 6:
            self.hand.cards = np.append(self.hand.cards, self.cards[:6 - len(self.hand.cards)])
            self.cards = self.cards[6 - len(self.hand.cards):]
            return True
        return False
        
        
    def __init__(self):
        self.name = 'Deck'
        # Create random cards from 2 to 99
        self.cards = np.random.randint(2, 100, 98)

        # Create Hand
        self.hand = Hand(8)

        # Create Piles
        self.pile1 = UpwardPile()
        self.pile2 = UpwardPile()
        self.pile3 = DownwardPile()
        self.pile4 = DownwardPile()
    

class Challenge:
    def __init__(self):
        self.name = 'The Challenge'
    
    def new_game(self):
        # Create Deck
        self.deck = Deck()
        return True