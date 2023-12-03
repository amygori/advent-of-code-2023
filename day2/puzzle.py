import sys
from pathlib import Path


def do_the_thing(input):
    sum_of_powers = 0

    for game_record in input:
        max_red = 0
        max_blue = 0
        max_green = 0
        game, sets = game_record.split(":")
        game_id = game[5:]
        sets = [set.split(", ") for set in sets.split(";")]
        for set in sets:
            for cubes in set:
                amount, color = cubes.strip().split(" ")
                if color == "red":
                    if max_red < int(amount):
                        max_red = int(amount)
                elif color == "green":
                    if max_green < int(amount):
                        max_green = int(amount)
                elif color == "blue":
                    if max_blue < int(amount):
                        max_blue = int(amount)
        print(f"Game {game_id}: red: {max_red} green: {max_green} blue: {max_blue}")
        power = max_red * max_green * max_blue
        sum_of_powers += power

    return sum_of_powers


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("Please provide a file")
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(do_the_thing(input))
    else:
        raise TypeError("This is not a file")
