import random
from enum import Enum

class Suit(Enum):
    Clubs = 0
    Diamonds = 1
    Hearts = 2
    Spades = 3

class Number(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

class Card:
    def __init__(self, number, suit):
        self.number = Number(number)
        self.suit = Suit(suit)

    def getCard(self):
        return (self.number.name + ' of ' + self.suit.name)

class Deck:
    contents = []

    def __init__(self):
        for num in Number:
            for suit in Suit:
                self.contents.append(Card(num.value, suit.value))

    def shuffleDeck(self):
        random.shuffle(self.contents)

    def printDeck(self):
        print("Deck contents:")
        for card in self.contents:
            print(card.getCard())
        print(" ")

    def dealCard(self, player):
        player.receiveCard(self.contents[0])
        self.contents.pop(0)

    def isEmpty(self):
        print('isEmpty check:' + str(len(self.contents)))
        return len(self.contents) == 0

class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []

    def receiveCard(self, card):
        self.hand.append(card)

    def playCard(self, index):
        card = hand[index]
        hand.pop(index)
        return card

    def sortHand(self):
        print("LUL")

    def showHand(self):
        print("Player ID", self.id, "hand:")
        for card in self.hand:
            print(card.getCard())
        print(' ')

class BidPhase:
    def __init__(self, players):
        self.players = players

    def generateConclusion(self):
        return 'C', 0

    def startBidding(self):
        print(0)
