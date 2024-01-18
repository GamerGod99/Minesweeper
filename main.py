from random import shuffle


IMG = {
    'n0': ' ',
    'n1': '1',
    'n2': '2',
    'n3': '3',
    'n4': '4',
    'n5': '5',
    'n6': '6',
    'n7': '7',
    'n8': '8',
    'n9': '*',
    'explosion': '#',
    'no_mine': 'X',
    'covered': '-',
    'flagged': '!'

}


class Tile:
    # States
    COVERED = 0
    UNCOVERED = 1
    FLAGGED = 2
    DETONATED = 3
    NO_MINE = 4
    MINE = 9

    def __init__(self, y, x, val):
        self.x = x
        self.y = y
        self.val = val
        self.state = Tile.COVERED

    def __repr__(self):
        if self.state == Tile.COVERED:
            return IMG['covered']
        elif self.state == Tile.FLAGGED:
            return IMG['flagged']
        elif self.state == Tile.DETONATED:
            return IMG['explosion']
        elif self.state == Tile.NO_MINE:
            return IMG['no_mine']
        elif self.state == Tile.UNCOVERED:
            return IMG[f'n{self.val}']
        return str(self.val)


class Minesweeper:

    around = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),
    ]

    def __init__(self, size_x, size_y, mine_amount):

        self.size_x = size_x
        self.size_y = size_y
        self.mine_amount = mine_amount
        self.plane = self.__plant()

    def __repr__(self):
        return '\n' + '\n'.join('\t' + ' '.join(str(tile) for tile in row) for row in self.plane) + '\n'

    def __plant(self):

        mines = [0] * (self.size_x * self.size_y - self.mine_amount) + [Tile.MINE] * self.mine_amount
        shuffle(mines)

        plane = []

        for row in range(self.size_y):
            temp = []
            for column in range(self.size_x):
                temp.append(Tile(row, column, mines[row * self.size_x + column]))
            plane.append(temp)

        for row in range(self.size_y):
            for column in range(self.size_x):

                if plane[row][column].val != Tile.MINE:
                    mines_adjacent = 0

                    for step_y, step_x in Minesweeper.around:
                        y = row + step_y
                        x = column + step_x

                        if 0 <= y < self.size_y and 0 <= x < self.size_x:
                            if plane[y][x].val == Tile.MINE:
                                mines_adjacent += 1

                    plane[row][column].val = mines_adjacent

        return plane

    def check_tile(self, column: int = 0, row: int = 0) -> int:
        if 0 <= column < SIZE_Y and 0 <= row < SIZE_X:
            return plane[row][column].val
        else:
            return -1

    def uncover_on_start(self, y, x):
        if 0 <= y < SIZE_Y and 0 <= x < SIZE_X:

            tile = plane[y][x]
            if tile.state == Tile.COVERED:
                if tile.val == 0:
                    tile.state = Tile.UNCOVERED
                    for step_y, step_x in around:
                        uncover_on_start(y + step_y, x + step_x)
                elif tile.val == 9:
                    pass  # GAME OVER
                else:
                    tile.state = Tile.UNCOVERED
        pass


def print_plant(m):
    pass


if __name__ == '__main__':

    # plant_mines()
    # plant_numbers()
    # print_plane()
    # print()

    ms = Minesweeper(10, 10, 15)
    print_plant(ms)
    print(ms)

    # GAME LOOP
    while True:
        user_x = input('Enter x coordinate: ')
        if user_x == '': break
        user_y = input('Enter y coordinate: ')
        if user_y == '': break

        user_x = int(user_x)
        user_y = int(user_y)
        print(uncover_on_start(user_x, user_y))
        print_plane()
