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
        print("Deck contents:")
        for card in self.contents:
            print(card.number, end="")
            print(card.suit, end=" ")
        print(" ")

    def dealCard(self, player, count=1):
        for i in range(0, count):
            player.receiveCard(self.contents[0])
            self.contents.pop(0)

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

    def showHand(self):
        print("Player ID", self.id, "hand:")
        for card in self.hand:
            print(card.number, end="")
            print(card.suit, end=" ")
        print(" ")

class Game:
    def __init__(self, deck, playerOne, playerTwo, playerThree, playerFour):
        self.deck = deck
        self.p1 = playerOne
        self.p2 = playerTwo
        self.p3 = playerThree
        self.p4 = playerFour

    

deck = Deck()
player = Player(0)
deck.dealCard(player)
deck.dealCard(player)
deck.dealCard(player)
deck.printDeck()
player.showHand()
