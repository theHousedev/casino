import random
from enum import Enum
from typing import override
from dataclasses import dataclass


class Suit(Enum):
    spade = 1   # ♠
    heart = 2   # ♥
    club = 3    # ♣
    diamond = 4  # ♦


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

    @override
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


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()

    def size(self):
        return len(self.cards)


class Player:
    def __init__(self, index: int):
        self.hand: list[Card] = []
        self.stack: list[Card] = []
        self.i: int = index
        self.active: bool = False

    def toggleActive(self):
        self.active = not self.active

    def showHand(self):
        handString = "  ".join(str(card) for card in self.hand)
        return handString


class Players:
    def __init__(self, numPlayers: int):
        self._players: dict[int, Player] = {}
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
        self.deck: Deck = Deck()
        self.table: list[Card] = []
        self.round: int = 0
        self.maxRounds: int = int(12 / numPlayers)
        self.players: Players = Players(numPlayers)
        self.playerIndex: int = 1
        self.activePlayer: Player = self.players[self.playerIndex]

    def turn(self, player: Player):
        if self.round > 1:
            self.showTable()
        self.showPlayer(player)

    def showTable(self):
        tableString = "  ".join(str(card) for card in self.table)
        print("-----------------------------")
        print(f"Table:     {tableString}")
        print("-----------------------------")

    def dealRound(self):
        for i in range(4):
            for player in self.players:
                player.hand.append(self.deck.deal())
            if self.round == 1:
                self.table.append(self.deck.deal())

    def newRound(self):
        self.round += 1
        self.dealRound()
        self.showTable()

    def showPlayer(self, player: Player):
        print(f"Player {player.i}:  {player.showHand()}")
        print("-----------------------------")

    def getActivePlayer(self) -> Player:
        return self.players[self.playerIndex]

    def nextPlayer(self):
        if self.playerIndex == len(self.players):
            self.playerIndex = 1
        else:
            self.playerIndex += 1
        self.activePlayer = self.players[self.playerIndex]

    def end(self):
        print(f"Game over!")
        # display results: player card counts & captures, scored points
        print("-----------------------------")


def runGame(numPlayers: int):

    # prompt for game start input

    game = Game(numPlayers)

    while game.deck.size() > 0:
        game.newRound()
        while any(player.hand for player in game.players):
            DEBUG_incrementTurn(game)
        game.table = []
    game.end()

    # prompt for game start input with restart=true,
    # which keeps running total score and number of won games
    #     save running totals to file (json, yaml?)


def DEBUG_incrementTurn(game: Game):
    if game.round == 1:
        print(f"[DEBUG] Max rounds: {game.maxRounds}")

    print(f"[DEBUG] Current round: {game.round}")
    print(f"[DEBUG] Active player: {game.getActivePlayer().i}")
    print(f"[DEBUG] Active player hand: {game.activePlayer.showHand()}")
    print(f"[DEBUG] Remaining cards: {game.deck.size()}")
    print(f"Press enter to increment turn...")
    _ = input()
    _ = game.activePlayer.hand.pop()
    game.nextPlayer()


def main():
    runGame(numPlayers=4)


if __name__ == "__main__":
    main()
