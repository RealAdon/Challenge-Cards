import numpy as np

class Pile:
    def __init__(self):
        self.name = 'Pile'
        self.played_cards = []
        self.direction = 'up'
    
    def play_card(self, card):
        # If the card is greater than the top card or exactly ten smaller than the top card, play the card
        if self.direction == 'up':
            if card > self.top_card or card == self.top_card - 10:
                self.top_card = card
                # self.played_cards.append(card)
                return True
        # If the card is smaller than the top card or exactly ten greater than the top card, play the card
        else:
            if card < self.top_card or card == self.top_card + 10:
                self.top_card = card
                # self.played_cards.append(card)
                return True
        return False
    
    def check_card(self, card):
        if self.direction == 'up':
            # If the card is greater than the top card or exactly ten smaller than the top card, return True
            if card > self.top_card or card == self.top_card - 10:
                return True
        else:
            # If the card is smaller than the top card or exactly ten greater than the top card, return True
            if card < self.top_card or card == self.top_card + 10:
                return True
        return False

class UpwardPile(Pile):
    def __init__(self):
        self.name = 'UpwardPile'
        self.top_card = 1
        self.direction = 'up'

class DownwardPile(Pile):
    def __init__(self):
        self.name = 'DownwardPile'
        self.top_card = 100
        self.direction = 'down'

class Hand:
    def __init__(self, max_cards) -> None:
        self.cards = np.array([])
        self.max_cards = max_cards

class Deck:
    def deal_cards(self):
        # If the hand size is smaller than 6 fill up to the hand max size
        if len(self.hand.cards) <= self.hand.max_cards - 2:
            cards_to_draw = self.hand.max_cards - len(self.hand.cards)
            # Fill up to the max card amount
            self.hand.cards = np.append(self.hand.cards, self.cards[:cards_to_draw])
            # Remove the cards from the deck
            self.cards = self.cards[cards_to_draw:]
            print(len(self.cards))
            # Sort the hand from min to max
            self.hand.cards = np.sort(self.hand.cards)
            return True
        return False
        
        
    def __init__(self):
        self.name = 'Deck'
        # Create random cards from 2 to 99
        self.cards = np.random.randint(2, 100, 98).astype(int)

        # Create Piles
        self.pile1 = UpwardPile()
        self.pile2 = UpwardPile()
        self.pile3 = DownwardPile()
        self.pile4 = DownwardPile()

        # Create Hand
        self.hand = Hand(8)

        # Deal cards
        self.deal_cards()

    def check_possible_moves(self):
        # Check if the hand has any possible moves
        return any(pile.check_card(card) for card in self.hand.cards for pile in [self.pile1, self.pile2, self.pile3, self.pile4])
    
    def check_state_of_challenge(self):
        # If the hands and the deck are empty, the game is won
        if len(self.hand.cards) == 0 and len(self.cards) == 0:
            return 'won'
        # If the hand size is greater than max_cards - 2 and there are no possible moves, the game is lost
        elif len(self.hand.cards) > self.hand.max_cards - 2 and not self.check_possible_moves():
            return 'lost'
        # If there are no possible moves and the the card size is smaller or equal to max_cards - 2, cards can be drawn
        elif not self.check_possible_moves() and len(self.hand.cards) <= self.hand.max_cards - 2:
            return 'draw'
        return 'ongoing'
    
    def play_card(self, card, pile):
        # If the card is in the hand and the pile is valid, play the card
        if card in self.hand.cards and pile in ['pile1', 'pile2', 'pile3', 'pile4']:
            # Play the card
            if eval(f'self.{pile}.play_card(card)'):
                # Remove the card from the hand
                self.hand.cards = np.delete(self.hand.cards, np.where(self.hand.cards == card))
                return True
        return False

class Challenge:
    def __init__(self):
        self.name = 'The Challenge'
    
    def new_game(self):
        # Create Deck
        self.deck = Deck()
        return True