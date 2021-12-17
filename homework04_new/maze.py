from copy import deepcopy
from random import choice, randint

ignore_missing_imports = True
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    x = coord[0]
    y = coord[1]
    to_where = choice(("up", "right"))
    if x > 2 and x % 2 != 0 and (y == len(grid[0]) - 2 or to_where == "up"):
        grid[x - 1][y] = " "
    elif y < len(grid[0]) - 3 and y % 2 != 0 and (x == 1 or to_where == "right"):
        grid[x][y + 1] = " "
    return grid


def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    # генерация входа и выхода
    for i, cell in enumerate(empty_cells):
        remove_wall(grid, cell)

    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """
    exit_here = []
    for x, row in enumerate(grid):
        if "X" in row:
            for y, _ in enumerate(row):
                if grid[x][y] == "X":
                    exit_here.append((x, y))
            if len(exit_here) == 2:
                break
    return exit_here


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
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
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    x, y = exit_coord
    path = [(x, y)]
    k = int(grid[x][y]) + 1
    while k != 1:
        k -= 1
        if x - 1 >= 0 and grid[x - 1][y] == k - 1:
            grid[x - 1][y] = k + 1
            x -= 1
            path.append((x, y))
            continue
        if x + 1 < len(grid) and grid[x + 1][y] == k - 1:
            grid[x + 1][y] = k + 1
            x += 1
            path.append((x, y))
            continue
        if y - 1 >= 0 and grid[x][y - 1] == k - 1:
            grid[x][y - 1] = k + 1
            y -= 1
            path.append((x, y))
            continue
        if y + 1 < len(grid[x]) and grid[x][y + 1] == k - 1:
            grid[x][y + 1] = k + 1
            y += 1
            path.append((x, y))
            continue
    if len(path) != grid[exit_coord[0]][exit_coord[1]]:
        grid[path[-1][0]][path[-1][1]] = " "
        path.pop(len(path) - 1)
        shortest_path(grid, exit_coord)
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    x, y = coord
    if x == 0 and grid[x + 1][y] != " ":
        return True
    if x == len(grid) - 1 and grid[x - 1][y] != " ":
        return True
    if y == 0 and grid[x][y + 1] != " ":
        return True
    if y == len(grid[0]) - 1 and grid[x][y - 1] != " ":
        return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
    exit_here = get_exits(grid)
    if len(exit_here) == 1:
        return grid, exit_here[0]

    if encircled_exit(grid, exit_here[0]) or encircled_exit(grid, exit_here[1]):
        return grid, None

    in_, out = exit_here

    grid[in_[0]][in_[1]], grid[out[0]][out[1]] = 1, 0

    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == " ":
                grid[x][y] = 0
    k = 0
    while grid[out[0]][out[1]] == 0:
        k += 1
        grid = make_step(grid, k)

    path = shortest_path(grid, out)
    return grid, path


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for x, row in enumerate(grid):
            for y, _ in enumerate(row):
                if grid[x][y] != "■":
                    grid[x][y] = " "
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
