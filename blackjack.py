# classes - Deck, Card, Dealer, Player, Game
# create the deck
# shuffle
# add player and Dealer 
# deal cards
# play hand

import random
SUITS = ['♥️','♦️','♠️','♣️']
RANKS = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)
                

    def __str__(self):
        deck_string = ''
        for card in self.cards:
            deck_string += ' ' +  str(card)
            
        return deck_string
        
        
    
    def shuffle(self):
        random.shuffle(self.cards)

class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return 'Dealer'
    
    def hit(self, card):
        # deal an indiviadua card
        self.hand.append(card)
    
class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name
    
    def choice(self):
        choice = input('Would you like to (h)it or (s)tay ')
        return choice

class Game:
    def __init__(self, suits, ranks):
        self.player = Player(self.get_player_name())
        self.dealer = Dealer()
        self.deck = Deck(suits, ranks)
        self.deck.shuffle()
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        # self.show_cards(self.dealer)

    def get_player_name(self):
        name = input('What is your name? ')
        return name
    
    def deal_card(self, person):
        card = self.deck.cards.pop()
        person.hand.append(card)

    def show_cards(self, person):
        rank_value = []
        print(f'{person} has: ')
        for card in person.hand:
            if isinstance(card.rank, int):
                rank_value.append(card.rank)
            elif card.rank == 'A':
                rank_value.append(11)
            else:
                rank_value.append(10)

            print(card)
        print(f"The value of {person}'cards is {sum(rank_value)}")
        return sum(rank_value)

        

    def player_hand(self):
        choice = self.player.choice()
        if choice == 'h':
            self.deal_card(self.player)

new_game = Game(SUITS, RANKS)
dealer_score = new_game.show_cards(new_game.dealer)
print(dealer_score)
player_score = new_game.show_cards(new_game.player)
print(player_score)



keep_playing = 0

while keep_playing < 21:
    new_game.player_hand()
    current_score  = new_game.show_cards(new_game.player)
    keep_playing  += current_score
else:
    print("I am sorry but you lost")
    another_game = Game(SUITS, RANKS)













