from copy import deepcopy

import pygame

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

        self.cell_size = cell_size
        self.width = cell_size * self.life.cols
        self.height = cell_size * self.life.rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.speed = speed
        self.paused = False

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for y in range(self.life.rows):
            for x in range(self.life.cols):
                if self.life.curr_generation[y][x] == 0:
                    color = "white"
                else:
                    color = "green"
                pygame.draw.rect(
                    self.screen,
                    pygame.Color(color),
                    [x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size],
                )

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        while running:
            self.life.step()
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    life0 = GameOfLife((80, 80), max_generations=50)
    game = GUI(life0)
    game.run()
