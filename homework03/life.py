import pathlib
import random
import typing as tp

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        self.rows, self.cols = size
        self.prev_generation = self.create_grid()
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_generations = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [[random.choice([0, 1]) in range(self.cols)] for j in range(self.rows)]
        else:
            return [[0 in range(self.cols)] for j in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        cells = []
        y = cell[0]
        x = cell[1]
        if y - 1 >= 0:
            cells.append(self.curr_generation[y - 1][x])
        if y + 1 < self.rows:
            cells.append(self.curr_generation[y + 1][x])
        if x - 1 >= 0:
            if y - 1 >= 0:
                cells.append(self.curr_generation[y - 1][x - 1])
            cells.append(self.curr_generation[y][x - 1])
            if y + 1 < self.rows:
                cells.append(self.curr_generation[y + 1][x - 1])
        if x + 1 < self.cols:
            if y - 1 >= 0:
                cells.append(self.curr_generation[y - 1][x + 1])
            cells.append(self.curr_generation[y][x + 1])
            if y + 1 < self.rows:
                cells.append(self.curr_generation[y + 1][x + 1])
        return cells

    def get_next_generation(self) -> Grid:
        updated_grid = []
        for y in range(0, self.rows):
            row = []
            for x in range(0, self.cols):
                if sum(self.get_neighbours((y, x))) == 3 or (
                    self.curr_generation[y][x] == 1 and sum(self.get_neighbours((y, x))) == 2
                ):
                    row.append(1)
                else:
                    row.append(0)
            updated_grid.append(row)
        return updated_grid

    def step(self) -> None:
        if not self.is_max_generations_exceeded and self.is_changing:
            self.prev_generation = self.curr_generation
            self.curr_generation = self.get_next_generation()
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        if self.max_generations is not None:
            return self.generations >= self.max_generations
        else:
            return False

    @property
    def is_changing(self) -> bool:
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        file = open(filename, "r")
        file_grid = file.read().split()
        new_grid = []
        for i, row in enumerate(file_grid):
            new_grid.append(list(map(int, list(row))))
        grid = GameOfLife((len(file_grid), len(file_grid[0])))
        grid.curr_generation = new_grid
        return grid

    def save(self, filename: pathlib.Path) -> None:
        file = open(filename, "w")
        for i in self.curr_generation:
            file.write("".join(list(map(str, i))) + "\n")
        file.close()
