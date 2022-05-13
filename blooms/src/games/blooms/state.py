from abc import ABC
from copy import deepcopy
from typing import Optional

from typing import Optional
from src.games.blooms.action import Connect4Action
from src.games.blooms.result import Connect4Result
from src.games.state import State
from src.games.blooms.player import Connect4Player
from src.games.player import Player
import colorama
from colorama import Fore
from colorama import init
init(autoreset=True)


class Connect4State(State):
    EMPTY_CELL = -1

    def __init__(self):
        super().__init__()

        # management board
        self.board_01 = [[0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                         [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                         [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]]

        # interface board
        self.board_x = [["-", "-", "-", " ", "-", " ", "-", " ", "-", " ", "-", "-", "-"],
                        ["-", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", "-"],
                        ["-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-"],
                        [" ", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", " "],
                        ["-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-"],
                        ["-", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", "-"],
                        ["-", "-", "-", " ", "-", " ", "-", " ", "-", " ", "-", "-", "-"]]


        # if num_rows < 4:
        # raise Exception("the number of rows must be 4 or over")
        # if num_cols < 4:
        # raise Exception("the number of cols must be 4 or over")

        """
        the dimensions of the board
        """
        # self.__num_rows = num_rows
        # self.__num_cols = num_cols

        """
        the grid
        """
        # self.__grid = [[Connect4State.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    """
    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False
    """

    # print management board
    def print_board_x(self):
        n=0
        print('  0 1 2 3 4 5 6 7 8 9|10|11|12')
        for r in self.board_x:
            print(n, end='')
            n = n + 1
            hexanterior = 1
            for c in r:
                if c == '-':
                    if hexanterior == 1:
                        print(r'  ', end='')
                        hexanterior = 1
                    continue
                else:

                    print(fr'{Fore.RED}/{Fore.BLUE}{c}{Fore.RED}\ ', end='')
                    hexanterior = 0
            print()
            # print(c, end=" ")
            hexanterior = 1
            print(' ', end='')
            for c in r:
                if c == '-':
                    if hexanterior == 1:
                        print(r'  ', end='')
                        hexanterior = 1
                    continue
                else:
                    print(Fore.RED + r'\_/ ', end='')
                    hexanterior = 0
            print()


    # print interface board
    def print_board_01(self):
        for r in self.board_01:
            for c in r:
                print(c, end=" ")
            print()

    def get_board_01(self):
        return self.board_01

    def get_board_x(self):
        return self.board_x

    def get_num_players(self):
        return 2

    def directNeighbors(self, x, y):
        hex_directions = [(0, -2), (-1, -1), (0, 2), (-1, 1), (1, 1), (1, -1)]
        direct_neighbors = []
        for list_item in hex_directions:
            g = x + list_item[0]
            z = y + list_item[1]
            if self.board_01[g][z] == 0:
                print("Valor fora do limite do tabuleiro")
                continue

            direct_neighbors.append((g, z))
            # print(f"({g},{z})")
            # print(self.board_01[g][z])
            """
            copy self.board_01, self.territory_board
            if self.territory_board_01[g][z] == self.board_01[x][y]
                self.territory_board_01[g][z]= -1 
                check_neighbor(g,z)       
            if self.territory_board_01[g][z] == 0:
                #print("Valor fora do limite do tabuleiro")
                continue
            if self.territory_board_01[g][z] == -1:
                continue
            """
        return direct_neighbors

    def findNeighbors(self, x, y, number, visited=None):
        if visited is None:
            visited = set()
        for list_item in self.directNeighbors(x, y):
            g = list_item[0]
            z = list_item[1]
            # visit node if it’s new
            if list_item not in visited:
                visited.add(list_item)

                # go recursively if the new node is green
                if self.board_01[g][z] == number:
                    self.findNeighbors(g, z, number, visited)

        return visited



    def validate_action(self, action: Connect4Action) -> bool:
        pos = action
        x = pos.get_x()
        y = pos.get_y()

        if self.board_01[x][y] == 0:
            return False

        return True

    def update(self, action: Connect4Action):
        # col = action.get_col()
        x = action.get_x()
        y = action.get_y()

        # colors for player 0
        # self.board_01[x][y] = self.__player_to_play
        if self.get_acting_player() == 0:
            self.board_x[x][y] = 2
            self.board_01[x][y] = 2

        # colors for player 1
        if self.get_acting_player() == 1:
            self.board_x[x][y] = 3
            self.board_01[x][y] = 3

        # pelo que entendi... isso dá get da coluna que o player selecionou para jogar
        # e dá update o board...e define essa coluna como jogada pelo player
        # drop the checker
        """
        for row in range(self.__num_rows - 1, -1, -1):
            if self.__grid[row][col] < 0:
                self.__grid[row][col] = self.__player_to_play
                break
        """

        # print(self.__player_to_play)
        # falta ajustar o valor 2 para ser relativo ao jogador atual
        visited = self.findNeighbors(x, y, 2)
        print(visited)
        # determine if there is a winner
        # IMPLEMENTAR
        # self.__has_winner = self.__check_winner(self.__player_to_play)
        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0
        self.__turns_count += 1



    """
    def __display_cell(self, row, col):
        print({
            0:                              '\033[91mR\033[0m',
            1:                              '\033[94mB\033[0m',
            Connect4State.EMPTY_CELL:       ' '
        }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            print('|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")
    """

    def __is_full(self) -> bool:
        count = 0
        for row in self.board_01:
            for col in row:
                if col == 1:
                    count = count + 1
        if count == 0:
            return True
        return False

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        return deepcopy(self)


    """
    def get_result(self, pos) -> Optional[Connect4Result]:
        if self.__has_winner:
            return Connect4Result.LOOSE if pos == self.__acting_player else Connect4Result.WIN
        if self.__is_full():
            return Connect4Result.DRAW
        return None
    """

    """
    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols
    """

    def display(self):
        self.print_board_x()

    def get_result(self, pos):
        pass

    def before_results(self):
        pass
