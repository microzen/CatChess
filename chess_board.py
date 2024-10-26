from inspect import stack

_ROW = 8
_COL = 8
_CELL_HEIGHT = 100
_CELL_WIDTH = 100
COLOR = [[(199, 142, 83), (0, 0, 0)], [(247, 208, 164), (255, 255, 255)]]


class Board:

    def __init__(self, pygame):
        self.focus = (-1, -1)
        self.board = []
        self.game = pygame
        for i in range(_ROW):
            row = []
            for j in range(_COL):
                row.append(self.game.Rect(j * _CELL_HEIGHT, i * _CELL_WIDTH, _CELL_WIDTH, _CELL_HEIGHT))
                self.game.draw.rect(self.game.display.get_surface(), COLOR[(i + j) % 2][0], row[j])
            self.board.append(row)

    def get_cell(self, row, col):
        return self.board[row][col]

    def move_in(self, row, col):
        if 0 <= row < _ROW and 0 <= col < _COL:
            if self.focus == (-1, -1):
                self.focus = (row, col)
                self.game.draw.rect(self.game.display.get_surface(), COLOR[(row + col) % 2][1], self.get_cell(row, col))
            elif self.focus != (row, col):
                self.game.draw.rect(self.game.display.get_surface(), COLOR[(self.focus[0] + self.focus[1]) % 2][0],
                                    self.get_cell(self.focus[0], self.focus[1]))
                self.focus = (row, col)
                self.focus = (-1, -1)
            else:
                return