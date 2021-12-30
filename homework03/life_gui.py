import pygame

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.width = 640
        self.height = 480
        self.cell_size = cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed
        self.paused = False

    def run(self) -> None:
        pass

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                if self.life.curr_generation[y // self.cell_size][x // self.cell_size] == 0:
                    color = "white"
                else:
                    color = "green"
                pygame.draw.rect(
                    self.screen, pygame.Color(color), [x, y, self.cell_size, self.cell_size]
                )