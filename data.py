import random
from enum import Enum
from dataclasses import dataclass
from typing import override

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