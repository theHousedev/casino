import random
from enum import Enum
from dataclasses import dataclass

class Suit(Enum):
    spade = 1   # ♠
    heart = 2   # ♥
    club = 3    # ♣
    diamond = 4 # ♦

class Rank(Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

@dataclass
class Card:
    suit: Suit
    rank: Rank

    def __str__(self):
        ranks = {
            Rank.ace: "A", Rank.two: "2", Rank.three: "3", Rank.four: "4",
            Rank.five: "5", Rank.six: "6", Rank.seven: "7", Rank.eight: "8",
            Rank.nine: "9", Rank.ten: "10", Rank.jack: "J", Rank.queen: "Q",
            Rank.king: "K"
        }
        suits = {
            Suit.spade: "♠", Suit.heart: "♥", Suit.club: "♣", Suit.diamond: "♦"
        }
        return f"{ranks[self.rank]}{suits[self.suit]}".rjust(3)

@dataclass
class Hand:
    cards: list[Card]

    def __str__(self):
        return "  ".join(str(card) for card in self.cards)

class Deck:
    def __init__(self):
        self.cards = []

        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, to: Hand=None, cards: int=1):
        dealtCards = []
        for i in range(cards):
            dealtCards.append(self.cards.pop(i))
        if to:
            to.cards.extend(dealtCards)
        return dealtCards

    def size(self):
        return len(self.cards)

class Player:
    def __init__(self, index: int):
        self.hand = Hand(cards=[])
        self.stack = Hand(cards=[])
        self.i = index

class Players:
    def __init__(self, numPlayers: int):
        self._players = {}
        for i in range(1, numPlayers + 1):
            self._players[i] = Player(index=i)

    def __getitem__(self, index: int):
        if index not in self._players:
            raise ValueError(f"Player {index} not found")
        return self._players[index]

    def __len__(self):
        return len(self._players)
    
    def __iter__(self):
        return iter(self._players.values())
    
    def keys(self):
        return self._players.keys()
    
    def values(self):
        return self._players.values()


class Game:
    def __init__(self, numPlayers: int):
        if numPlayers <2 or numPlayers > 4:
            raise ValueError("Number of players must be 2, 3, or 4")
        self.players = Players(numPlayers)
        self.deck = Deck()
        self.table = Hand(cards=[])
        self.round = 0
        self.maxRounds = int(12 / numPlayers)
        self.newRound()

    def newRound(self):
        self.round += 1
        for i in self.players.keys():
            self.deck.deal(to=self.players[i].hand, cards=4)
        self.deck.deal(to=self.table, cards=4)
        self.showTable()

    def turn(self, player: Player):
        if self.round > 1:
            self.showTable()
        self.showPlayer(player)

    def showTable(self):
        print("-----------------------------")
        print(f"Table:     {self.table}")
        print("-----------------------------")

    def showPlayer(self, player: Player):
        print(f"Player {player.i}:  {player.hand}")
        print("-----------------------------")

def main():
    game = Game(numPlayers=2)
    game.turn(game.players[1])
    game.turn(game.players[2])


if __name__ == "__main__":
    main()


