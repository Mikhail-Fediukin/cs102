import pathlib
import random
import typing as tp
from pprint import pp

import pygame
from pygame.locals import *

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
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [[random.choice([1, 0]) for i in range(self.cols)] for j in range(self.rows)]
        else:
            return [[0 for i in range(self.cols)] for j in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        cells = []
        x = cell[0]
        y = cell[1]
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
            cells.append(self.curr_generation[y - 1][x + 1])
            if y + 1 < self.rows:
                cells.append(self.curr_generation[y + 1][x + 1])
        return cells

    def get_next_generation(self) -> Grid:
        updated_grid = []
        for y in range(0, self.rows):
            row = []
            for x in range(0, self.cols):
                if sum(self.get_neighbours((x, y))) == 3 or (
                    self.curr_generation[y][x] == 1 and sum(self.get_neighbours((x, y))) == 2
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
        for i, row in enumerate(file_grid):
            file_grid[i] = list(map(int, list(row)))
        grid = GameOfLife((len(file_grid), len(file_grid[0])))
        grid.curr_generation = file_grid
        return grid

    def save(self, filename: pathlib.Path) -> None:
        file = open(filename, "w")
        for i in self.curr_generation:
            file.write("".join(list(map(str, i))) + "\n")
        file.close()


if __name__ == "__main__":
    life0 = GameOfLife.from_file(pathlib.Path("glider.txt"))
    pp(life0.curr_generation)
