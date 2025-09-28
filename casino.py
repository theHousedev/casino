import random
from gamelogic import Game
from data import Suit, Rank, Card, Deck


def runGame(numPlayers: int):

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
    if game.round == 1:
        print(f"[DEBUG] Max rounds: {game.maxRounds}")

    print(f"[DEBUG] Current round: {game.round}")
    print(f"[DEBUG] Active player: {game.getActivePlayer().i}")
    print(f"[DEBUG] Active player hand: {game.getActivePlayer().showHand()}")
    print(f"[DEBUG] Remaining cards: {game.deck.size()}")
    print(f"Press enter to increment turn...")
    _ = input()
    _ = game.getActivePlayer().cards.pop()
    game.nextPlayer()


def main():
    runGame(numPlayers=4)


if __name__ == "__main__":
    main()
