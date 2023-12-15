import sys
from pathlib import Path
import string, random, re, math
import functools as ft
from pprint import pprint


def do_the_thing(input):
    grid = create_grid(input)
    gear_ratios_sum = 0
    gear_sets = []
    for asterisk_position, neighbors in grid["asterisks"].items():
        gears = set()
        for coords in neighbors:
            # look up coords in number_coords
            # If not None, add to gears
            if grid["number_coords"].get(coords) is not None:
                gears.add(int(grid["number_coords"][coords]))
        if len(gears) == 2:
            gear_sets.append(gears)
    for gear_set in gear_sets:
        if len(gear_set) == 2:
            gear_ratios_sum += math.prod(gear_set)
    return gear_ratios_sum


def create_grid(input):
    grid = {"asterisks": {}, "number_coords": {}}
    for y in range(len(input)):
        current_number = ""
        coords = []
        # record numbers and positions
        # then when you hit an asterisk, record the location of the asterisk
        for x in range(len(input[y])):
            neighbors = set()
            char = input[y][x]
            if char in string.digits:
                current_number += char
                coords.append((x, y))
                if x == 139 and current_number:
                    for coord in coords:  
                        grid["number_coords"][coord] = current_number
                    current_number = ""
                    coords = []
            else:
                if current_number:
                    for coord in coords:
                        grid["number_coords"][coord] = current_number
                    current_number = ""
                    coords = []
                if char == "*":
                    neighbors.update(get_neighbors(input, (x, y)))
                    grid["asterisks"][(x, y)] = neighbors
    return grid


def get_neighbors(grid, coords):
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
    elif y == len(grid) - 1:  # bottom row
        below = None
        below_left = None
        below_right = None
    if x == 0:  # left column
        left = None
        above_left = None
        below_left = None
    elif x == len(grid) - 1:  # right column
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
        input = Path.read_text(file).splitlines()
        print(do_the_thing(input))
    else:
        raise TypeError("This is not a file")
