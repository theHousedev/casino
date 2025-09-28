import random
from core import Game
from models import Suit, Rank, Card, Deck


def runGame(numPlayers: int):

    print(f"Starting game with {numPlayers} players")
    print(f"Press enter to start...")
    _ = input()

    # prompt for game start input

    game = Game(numPlayers)

    while game.deck.size() > 0:
        game.newRound()
        while any(player.cards for player in game.players):
            DEBUG_incrementTurn(game)
        game.table = []
    game.end()

    # prompt for game start input with restart=true,
    # which keeps running total score and number of won games
    #     save running totals to file (json, yaml?)

def DEBUG_incrementTurn(game: Game):
    print(f"[DEBUG] Round: {game.round}")
    print(f"[DEBUG] Player: {game.getActivePlayer().index}")
    print(f"[DEBUG] Hand: {game.getActivePlayer().showHand()}")
    print(f"[DEBUG] Deck: {game.deck.size()}")
    print(f"Press enter to play turn...")
    _ = input()

    game.playTurn(game.getActivePlayer())


def main():
    runGame(numPlayers=4)


if __name__ == "__main__":
    main()
