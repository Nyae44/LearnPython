# We are going to build a Python project based of the OOP knowledge learnt
# We are going to learn how classes can communicate with each other

# Card
# suit, rank value
import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10, 'Jack':11,'Queen':12,'King':13,'Ace':14}
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
two_hearts = Card("Hearts", "Two")
print(two_hearts)

three_of_clubs = Card('Club','Three')
print(three_of_clubs)
print(three_of_clubs.suit)
print(three_of_clubs.rank)
print(three_of_clubs.values)

# Deck class 
"""
- Instantiate a new Deck
    - Create all 52 objects 
    - Hold a list of cards as objects 
- Shuffle a Deck through a method call
    - Random library shuffle() function
- Deal cards from the Deck object
    - Pop method from cards list
"""

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
        
new_deck = Deck()
first_card = new_deck.all_cards[0]
print(first_card)
bottom_card = new_deck.all_cards[-1]
print(bottom_card)

# Print all cards 
'''
for card_object in new_deck.all_cards:
    print(card_object)
'''
new_deck.shuffle()
print(new_deck.all_cards[-1])


my_card = new_deck.deal_one()
print(my_card)

print(len(new_deck.all_cards))

'''
Player Class
    - This class will be used to hold a player's current list of cards
    - A player should be able to add or remove cards from their hand (list of card objects)
    - Translating a Deck/Hand of cards with a top and bottom to a Python list 
    
'''

class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # single card object
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    
new_player = Player("Daley")
print(new_player)
print(my_card)
new_player.add_cards(my_card)
print(new_player)
# Add multiple card objects
new_player.add_cards([my_card,my_card,my_card,my_card])
print(new_player)
new_player.remove_one()
print(new_player)

# Game Logic 

'''
- Create two instances of the player class
    - player_1
    - player_2
- Create an instance of the new deck
    - Half deck to player_1 
    - Half deck to player_2
- Check for 0 cards 
- Outer while loop passed boolean values to state if game is still on
- Logic to draw additional cards 
'''
# Game setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
# check if it works 

print(len(player_one.all_cards))

game_on = True

# counter 
round_num = 0 

while game_on:
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        print('player one, out of cards, player 2 wins')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('player two, out of cards, player 1 wins')
        game_on = False
        break
    
    # start a new round 
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    # check player's cards against each other
    '''
    player one > player two
    player one < player two
    player one == player two
    
    - state at_war = False if the players resolve the match-up,
      on first drawn card, otherwise we will add cards to the current,
      cards on the table.
    - RULES: Each player needs to draw 5 additional cards in case of a tie.
    - A player loses if they dont have at least 5 cards to play the war
    '''
     
    # at war
    # This occurs when the cards are equal.
    # We'll grab another card each and continue the current war.
            
    # First check to see if player has enough cards
            
    # Check to see if a player is out of cards:
    at_war = True
    while at_war:
        if player_one_cards[-1] > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            
            at_war = False
    
        else:
            print('WAR')
            
            if len(player_one.all_cards) < 5:
                print("Player one unable to declare war")
                print("Player two wins")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player two unable to declare war")
                print("Player one wins")
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    