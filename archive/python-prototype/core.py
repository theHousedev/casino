from models import Card, Deck


class Player:
    def __init__(self, index: int):
        self.cards: list[Card] = []
        self.stack: list[Card] = []
        self.index: int = index

    def showHand(self):
        handString = "  ".join(str(card) for card in self.cards)
        return handString

    def hasCards(self) -> bool:
        return len(self.cards) > 0


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
        self.activePlayerIndex: int = 1

    def showTable(self):
        tableString = "  ".join(str(card) for card in self.table)
        print("-----------------------------")
        print(f"Table:     {tableString}")
        print("-----------------------------")

    def playTurn(self, player: Player):
        self.showTable()

        # TODO: need to build actual interactive card selector
        playedCard = player.cards.pop()
        print(f"> {playedCard}")

        # TODO: card capture (simple 1:1 for now)
        capturedCards: list[Card] = []
        for tableCard in self.table:
            if tableCard.rank == playedCard.rank:
                capturedCards.append(tableCard)
                self.table.remove(tableCard)

        if capturedCards:
            for card in capturedCards:
                player.stack.append(card)
            player.stack.append(playedCard)
            print(f"Collected: {', '.join(str(c) for c in capturedCards)}") # DEBUG:
        else:
            self.table.append(playedCard)
            print(f"Trailed {playedCard} to table") # DEBUG:

        self.showTable()

    def nextPlayer(self):
        if self.activePlayerIndex == len(self.players):
            self.activePlayerIndex = 1
        else:
            self.activePlayerIndex += 1

    def dealRound(self):
        for i in range(4):
            for player in self.players:
                player.cards.append(self.deck.deal())
            if self.round == 1:
                self.table.append(self.deck.deal())

    def newRound(self):
        self.round += 1
        self.dealRound()

    def showPlayer(self, player: Player):
        print(f"Player {player.index}:  {player.showHand()}") # DEBUG:
        
    def isActivePlayer(self, player: Player) -> bool:
        return player.index == self.activePlayerIndex

    def getActivePlayer(self) -> Player:
        return self.players[self.activePlayerIndex]

    def end(self):
        print(f"Game over!")
        # TODO: calculate player scores.
        # for now just printing stacks:
        for i, p in enumerate(self.players):
            print("-----------------------------")
            print(f"Player {i} stack:")
            stackStr = ",".join(str(card) for card in p.stack)
            print(stackStr)
        print("-----------------------------")
