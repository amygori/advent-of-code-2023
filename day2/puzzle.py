import sys
from pathlib import Path

# 12 red cubes, 13 green cubes, and 14 blue cubes
RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14


def do_the_thing(input):
    sum_of_possible_games = 0
    for game_record in input:
        game, sets = game_record.split(":")
        game_id = game[5:]
        sets = [set.split(", ") for set in sets.split(";")]
        impossible = False
        for set in sets:
            for cubes in set:
                amount, color = cubes.strip().split(" ")
                if color == "red" and int(amount) > RED_LIMIT:
                    impossible = True
                    break
                elif color == "green" and int(amount) > GREEN_LIMIT:
                    impossible = True
                    break
                elif color == "blue" and int(amount) > BLUE_LIMIT:
                    impossible = True
                    break
            if impossible:
                break
        if not impossible:
            sum_of_possible_games += int(game_id)

    return sum_of_possible_games


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("Please provide a file")
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(do_the_thing(input))
    else:
        raise TypeError("This is not a file")
