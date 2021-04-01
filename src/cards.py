import random

class Card:
    def __init__(self, suit: str, rank: int):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = []
        self.newdeck()
        self.shuffle()
    
    def newdeck(self):
        for suit in ["Spades","Clubs","Hearts","Diamonds"]:
            for rank in range(1,14):
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    # def shuffle2(self):
    #     for a in range(len(self.deck)):
    #         b = random.randint(a,51)
    #         self.deck[a],self.deck[b] = self.deck[b],self.deck[a]

    def view(self):
        for card in self.deck:
            print(card)
