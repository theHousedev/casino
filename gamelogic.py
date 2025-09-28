from data import Card, Deck


class Player:
    def __init__(self, index: int):
        self.cards: list[Card] = []
        self.stack: list[Card] = []
        self.i: int = index
        self.active: bool = False

    def toggleActive(self):
        self.active = not self.active

    def showHand(self):
        handString = "  ".join(str(card) for card in self.cards)
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
        self.activePlayer: Player = self.players[self.playerIndex] # type: ignore

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
                player.cards.append(self.deck.deal())
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
        return self.players[self.playerIndex] # type: ignore

    def nextPlayer(self):
        if self.playerIndex == len(self.players):
            self.playerIndex = 1
        else:
            self.playerIndex += 1
        self.activePlayer = self.players[self.playerIndex] # type: ignore

    def end(self):
        print(f"Game over!")
        print("-----------------------------")