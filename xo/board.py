nrows = 3
ncols = 3
ncells = nrows * ncols


def is_player(piece):
    return piece == 'x' or piece == 'o'


def is_empty(piece):
    return not is_player(piece)


def other_player(player):
    if player == 'x':
        return 'o'
    elif player == 'o':
        return 'x'
    else:
        raise ValueError('expected a player: {}'.format(player))


class Board:
    @classmethod
    def fromstring(cls, layout=''):
        cells = [' '] * ncells

        for i, piece in enumerate(layout):
            if i >= ncells:
                break

            if is_player(piece):
                cells[i] = piece

        return cls(cells)

    # This should never be called directly. Use fromstring instead.
    def __init__(self, cells):
        self.cells = cells

    def __getitem__(self, pos):
        return self.cells[self._idx(*pos)]

    def __setitem__(self, pos, piece):
        self.cells[self._idx(*pos)] = self._normalize_to_piece(piece)

    def __iter__(self):
        return self._each_piece()

    def _each_piece(self):
        for i, piece in enumerate(self.cells):
            yield self._idx_to_row(i), self._idx_to_col(i), piece

    def toascii(self):
        return '\n---+---+---\n'.join([
            ' {} | {} | {} '.format(self.cells[0], self.cells[1], self.cells[2]),
            ' {} | {} | {} '.format(self.cells[3], self.cells[4], self.cells[5]),
            ' {} | {} | {} '.format(self.cells[6], self.cells[7], self.cells[8])
        ])

    def __str__(self):
        return ''.join(piece if is_player(piece) else '.' for piece in self.cells)

    @staticmethod
    def contains(r, c):
        return 1 <= r <= nrows and 1 <= c <= ncols

    @staticmethod
    def _normalize_to_piece(piece):
        if is_player(piece):
            return piece
        return E

    @classmethod
    def _idx(cls, r, c):
        if cls.contains(r, c):
            return ncols * (r - 1) + (c - 1)
        else:
            raise IndexError('position out of bounds: {}, {}'.format(r, c))

    @staticmethod
    def _idx_to_row(i):
        return i // ncols + 1

    @staticmethod
    def _idx_to_col(i):
        return i % ncols + 1