from core import Game


def runGame(numPlayers: int):

    print(f"Starting game with {numPlayers} players")
    print(f"Press enter to start...")
    _ = input()

    # prompt for game start input for real?

    game = Game(numPlayers)

    while game.deck.size() > 0:
        game.newRound()

        while any(player.cards for player in game.players):
            DEBUG_incrementTurn(game)

    game.end()

def DEBUG_incrementTurn(game: Game):
    print(f"[DEBUG] Round: {game.round}")
    print(f"[DEBUG] Player: {game.getActivePlayer().index}")
    print(f"[DEBUG] Hand: {game.getActivePlayer().showHand()}")
    print(f"Press enter to play turn...")
    _ = input()

    game.playTurn(game.getActivePlayer())

    game.nextPlayer()


def main():
    runGame(numPlayers=4)


if __name__ == "__main__":
    main()
