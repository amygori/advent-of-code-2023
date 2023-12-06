import sys
from pathlib import Path
import string
import random


def do_the_thing(input):
    grid = create_grid(input)
    sum = 0
    for num in grid["numbers"].keys():
        if any(coord in grid["symbols"] for coord in grid["numbers"][num]):
            print(f"Found a symbol nearby number {num}!")
            sum += int(num.split("-")[0])
        else:
            print(f"No symbols nearby number {num}!")
    return sum


def create_grid(input):
    grid = {"symbols": [], "numbers": {}, "number_coords": {}}
    neighbors = set()
    for y in range(len(input)):
        current_number = ""
        for x in range(len(input[y])):
            if input[y][x] in string.digits:
                current_number += input[y][x]
                adjacents = get_neighbors(input, (x, y))
                for neighbor in adjacents:
                    neighbors.add(neighbor)
            else:
                if current_number:
                    grid = record_number(grid, current_number, neighbors)
                    current_number = ""
                    neighbors = set()
                if input[y][x] != ".":
                    grid["symbols"].append((x, y))
            if x == len(input[y]) - 1:  # end of line
                if current_number:
                    grid = record_number(grid, current_number, neighbors)
                    neighbors = set()
    return grid


def record_number(grid, number, neighbors):
    unique_number = number + "-" + "".join(random.choices(string.ascii_letters, k=8))
    grid["numbers"][unique_number] = neighbors
    return grid


def get_neighbors(input, coords):
    x, y = coords
    above = (x, y - 1)
    below = (x, y + 1)
    left = (x - 1, y)
    right = (x + 1, y)
    above_left = (x - 1, y - 1)
    above_right = (x + 1, y - 1)
    below_left = (x - 1, y + 1)
    below_right = (x + 1, y + 1)
    if y == 0:  # top row
        above = None
        above_left = None
        above_right = None
    elif y == len(input) - 1:  # bottom row
        below = None
        below_left = None
        below_right = None
    if x == 0:  # left column
        left = None
        above_left = None
        below_left = None
    elif x == len(input) - 1:  # right column
        right = None
        above_right = None
        below_right = None
    neighbors = [
        above,
        above_right,
        right,
        below_right,
        below,
        below_left,
        left,
        above_left,
    ]
    return [neighbor for neighbor in neighbors if neighbor is not None]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("Please provide a file")
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(do_the_thing(input))
    else:
        raise TypeError("This is not a file")
