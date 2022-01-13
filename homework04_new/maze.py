from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:

    x, y = coord
    to_where = choice(["up", "right"])
    if x > 2 and x % 2 != 0 and (y == len(grid[0]) - 2 or to_where == "up"):
        grid[x - 1][y] = " "
    elif y < len(grid[0]) - 3 and y % 2 != 0 and (x == 1 or to_where == "right"):
        grid[x][y + 1] = " "
    return grid


def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        if x % 2 == 1:
            for y in range(len(row)):
                if y % 2 == 1:
                    grid[x][y] = " "
                    empty_cells.append((x, y))

    for cell in empty_cells:
        remove_wall(grid, cell)

    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        if x_in in (0, rows - 1):
            y_in = randint(0, cols - 1)
        else:
            y_in = choice((0, cols - 1))
        if x_out in (0, rows - 1):
            y_out = randint(0, cols - 1)
        else:
            y_out = choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"
    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:

    return [
        (x, y)
        for x, row in enumerate(grid)
        if "X" in row
        for y in range(len(row))
        if grid[x][y] == "X"
    ]


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:

    for x, row in enumerate(grid):
        for y in range(len(row)):
            if grid[x][y] == k:
                if x - 1 >= 0 and grid[x - 1][y] == 0:
                    grid[x - 1][y] = k + 1
                if x + 1 < len(grid) and grid[x + 1][y] == 0:
                    grid[x + 1][y] = k + 1
                if y - 1 >= 0 and grid[x][y - 1] == 0:
                    grid[x][y - 1] = k + 1
                if y + 1 < len(grid[x]) and grid[x][y + 1] == 0:
                    grid[x][y + 1] = k + 1
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:

    path = []
    x, y = exit_coord
    k = grid[x][y] + 1
    while k != 1:
        path.append((x, y))
        k -= 1
        if x < len(grid) - 1 and grid[x + 1][y] == k - 1:
            x += 1
            continue
        if x > 0 and grid[x - 1][y] == k - 1:
            x -= 1
            continue
        if y < len(grid[0]) - 1 and grid[x][y + 1] == k - 1:
            y += 1
            continue
        if y > 0 and grid[x][y - 1] == k - 1:
            y -= 1
            continue
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:

    x, y = coord
    if (
        (x == 0 and grid[x + 1][y] != " ")
        or (x == len(grid) - 1 and grid[x - 1][y] != " ")
        or (y == 0 and grid[x][y + 1] != " ")
        or (y == len(grid[0]) - 1 and grid[x][y - 1] != " ")
    ):
        return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:

    exit_here = get_exits(grid)

    if encircled_exit(grid, exit_here[0]) or encircled_exit(grid, exit_here[1]):
        return grid, None

    in_, out = exit_here
    grid[in_[0]][in_[1]], grid[out[0]][out[1]] = 1, 0
    for x, row in enumerate(grid):
        for y in range(len(row)):
            if grid[x][y] == " ":
                grid[x][y] = 0

    k = 0
    while grid[out[0]][out[1]] == 0:
        k += 1
        make_step(grid, k)
    return grid, shortest_path(grid, out)


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:

    if path:
        for x, row in enumerate(grid):
            for y in range(len(row)):
                if grid[x][y] != "■":
                    grid[x][y] = " "
                if (x, y) in path:
                    grid[x][y] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(5, 5)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(_, PATH)
    print(pd.DataFrame(MAZE))
