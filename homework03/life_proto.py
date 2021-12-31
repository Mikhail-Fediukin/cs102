import random
import typing as tp
from typing import List, Type

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid: Type[list[list[int]]] = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 1000, height: int = 500, cell_size: int = 20, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.draw_grid()
            self.draw_lines()
            self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [
                [random.choice([0, 1]) for i in range(self.cell_width)]
                for j in range(self.cell_height)
            ]
        else:
            return [[0 for i in range(self.cell_width)] for j in range(self.cell_height)]

    def draw_grid(self) -> None:
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                if self.grid[y // self.cell_size][x // self.cell_size] == 0:
                    color = "white"
                else:
                    color = "green"
                pygame.draw.rect(
                    self.screen, pygame.Color(color), [x, y, self.cell_size, self.cell_size]
                )

    def get_neighbours(self, cell: Cell) -> Cells:
        cells = []
        x = cell[1] // self.cell_size
        y = cell[0] // self.cell_size
        if y - 1 >= 0:
            cells.append(self.grid[y - 1][x])
        if y + 1 < self.cell_height:
            cells.append(self.grid[y + 1][x])
        if x - 1 >= 0:
            if y - 1 >= 0:
                cells.append(self.grid[y - 1][x - 1])
            cells.append(self.grid[y][x - 1])
            if y + 1 < self.cell_height:
                cells.append(self.grid[y + 1][x - 1])
        if x + 1 < self.cell_width:
            if y - 1 >= 0:
                cells.append(self.grid[y - 1][x + 1])
            cells.append(self.grid[y][x + 1])
            if y + 1 < self.cell_height:
                cells.append(self.grid[y + 1][x + 1])
        return cells

    def get_next_generation(self) -> Grid:
        updated_grid = []
        for y in range(0, self.height, self.cell_size):
            row = []
            for x in range(0, self.width, self.cell_size):
                if sum(self.get_neighbours((y, x))) == 3 or (
                    self.grid[y // self.cell_size][x // self.cell_size] == 1
                    and sum(self.get_neighbours((y, x))) == 2
                ):
                    row.append(1)
                else:
                    row.append(0)
            updated_grid.append(row)
        self.grid = updated_grid
        return self.grid


if __name__ == "__main__":
    game = GameOfLife()
    game.run()
