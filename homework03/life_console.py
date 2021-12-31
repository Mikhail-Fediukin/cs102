import curses
from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        screen.border("|", "|", "-", "-", "■", "■", "■", "■")

    def draw_grid(self, screen) -> None:
        for y, row in enumerate(self.life.curr_generation):
            for x, cell in enumerate(row):
                if cell == 1:
                    fill = "■"
                else:
                    fill = " "
                screen.addch(y + 1, x + 1, fill)

    def run(self) -> None:
        screen = curses.initscr()
        while True:
            self.life.step()
            self.draw_grid(screen)
            self.draw_borders(screen)
            screen.refresh()
            curses.napms(500)
        curses.endwin()
