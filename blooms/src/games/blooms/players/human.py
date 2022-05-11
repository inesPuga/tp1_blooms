from src.games.blooms.action import Connect4Action
from src.games.blooms.player import Connect4Player
from src.games.blooms.state import Connect4State


class HumanConnect4Player(Connect4Player):
    def __init__(self, name: str):
        super().__init__(name)

    def get_action(self, state: Connect4State) -> Connect4Action:
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                x, y = input(f"Player {state.get_acting_player()}, choose a space (x,y): ").split(",")
                return Connect4Action(int(x), int(y))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: Connect4State):
        # ignore
        pass

    def event_end_game(self, final_state: Connect4State):
        # ignore
        pass
