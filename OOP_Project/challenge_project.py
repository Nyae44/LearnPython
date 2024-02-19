# Create a blackjack game in Python

# import the random module - Allows us to shuffle the deck
import random


suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True

# Class definitions 
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit
    
# store 52 card objects 
class Deck():
    
    def __init__(self):
        self.deck = [] # start with an empty list 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
            return 'The deck has' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
# Testing Deck

test_deck = Deck()
print(test_deck)


# Hand class -> represents what cards are in someone's hand 
class Hand():
    
    def __init__(self):
        self.cards = [] # starts with an empty list like in the Deck class 
        self.value = 0 # start with zero value
        self.aces = 0 # add an attribute to keep track of aces 
    
    def add_card(self,card):
        # card passed in from Deck 
        # from Deck.deal() -> suit,rank
        self.cards.append(card)
        self.value += values[card.rank]
        
        # track Aces 
        if card == 'Ace':
            self.aces +=1
    def adjust_for_ace(self):
        # if total value > 21 and I still have an Ace
        # Change my Ace to be a 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            

# testing 

test_deck_ = Deck()
test_deck_.shuffle()

# Player
test_player = Hand()
# Deal 1 card pulled from the Deck(suit,rank)
pulled_card = test_deck_.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)


# implement chip class

class Chips():
    def __init__(self, total =100):
        self.total = total # This can be set to a default value or by user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
        
# functions for game play

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, please provide an integer!')
        else:
            if chips.bet > chips.Total:
                print('Sorry, you do not have enough chips! you have: {}'.format(chips.total))
            else:
                break
            
            
# Function taking hits

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    
# Function prompting the player to hit or stand
def hit_or_stand(deck,hand):
    global playing  # To control an upcoming while loop
    while True:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands Dealer's turn")
            playing = False
        else: 
            print("Sorry I did not understand that please enter h or s only")
            continue
        break
    

# Functions to display cards 

def show_some(player,dealer):
    # Show only one of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    # Show all (2 cards) of the player's hand/cards
    print("\n Player's hand")
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    # show all the dealer's cards 
    print("Dealer's hand")
    for card in dealer.cards:
        print(card)
    # We can also avoid the for loops and use the following code
    # sep = separator
    """
    print("Value of Dealer's hand is ",*dealer.cards, sep='\n')
    """
    # Calculate and display value(j+k == 20)
    print(f"Value of Dealer's hand is: {dealer.value}")
    # show all players cards
    print("\n Player hand")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")
    
# looping alternative 
items = [1,2,3]
for item in items:
    print(item)
    
# alternative
print("items: ",*items)

# functions to handle end of game scenarios
def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("PLAYER WINS")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("PLAYER WINS, DEALER BUSTED")
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("DEALER WINS")
    chips.win_bet()
def push(player,dealer):
    print("Dealer and player tie, PUSH")
    
# Game logic script