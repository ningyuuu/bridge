import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

class Deck:
    contents = []

    def __init__(self):
        for num in range(1,14):
            for suit in ['H', 'D', 'C', 'S']:
                self.contents.append(Card(num, suit))

    def shuffleDeck(self):
        random.shuffle(self.contents)

    def printDeck(self):
        for card in self.contents:
            print(card.number, end="")
            print(card.suit, end=" ")

class Player:

    hand = []

    def __init__(self, id):
        self.id = id

    def receiveCard(self, card):
        self.hand.append(card)

    def playCard(self, index):
        card = hand[index]
        hand.pop(index)
        return card


deck = Deck()
deck.shuffleDeck()
deck.printDeck()
