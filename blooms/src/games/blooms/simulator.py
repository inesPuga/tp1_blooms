from src.games.blooms.player import Connect4Player
from src.games.blooms.state import Connect4State
from src.games.game_simulator import GameSimulator
from src.games.state import State


class Connect4Simulator(GameSimulator):

    def __init__(self, player1: Connect4Player, player2: Connect4Player):
        super(Connect4Simulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the blooms grid
        """
        # self.__num_rows = num_rows
        # self.__num_cols = num_cols

    """
    def init_game(self):
        return Connect4State(self.__num_rows, self.__num_cols)
    """

    def init_game(self) -> State:
        return Connect4State()

    def before_end_game(self, state: Connect4State):
        # ignored for this simulator
        pass

    def end_game(self, state: Connect4State):
        # ignored for this simulator
        pass
