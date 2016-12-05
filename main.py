from library import *

class Game:
    def __init__(self, deck, playerOne, playerTwo, playerThree, playerFour):
        print("Initializing game")

        print("Add players to game")
        self.players = []
        self.players.append(playerOne)
        self.players.append(playerTwo)
        self.players.append(playerThree)
        self.players.append(playerFour)

        print("Preparing a deck")
        self.deck = deck

    def shuffleGameDeck(self):
        print ('Shuffling deck')
        self.deck.shuffleDeck()
        # self.deck.printDeck()

    def dealDeckToPlayers(self):
        print('Dealing deck')
        while not(self.deck.isEmpty()):
            for player in self.players:
                self.deck.dealCard(player)

        self.deck.printDeck()

        for player in self.players:
            player.sortHand()
            player.showHand()



    def startBidPhase(self):
        bidding = bidPhase(self.players)
        bidding.startBidding()

newGame = Game(Deck(), Player(0), Player(1), Player(2), Player(3))
