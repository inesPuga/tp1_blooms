from src.games.blooms.players.human import HumanConnect4Player
from src.games.blooms.simulator import Connect4Simulator
from src.games.blooms.players.custom import CustomConnect4Player


def main():
    sim = Connect4Simulator(
        HumanConnect4Player("Inês"),
        HumanConnect4Player("Gonçalo"),
    )

    sim.init_game()
    sim.run_simulation()

if __name__ == "__main__":
    main()