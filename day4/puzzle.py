import sys
from pathlib import Path
from pprint import pprint


def do_the_thing(input):
    total_points = 0
    for card in input:
        winning_nums = [int(num) for num in card.split(":")[1].split("|")[0].split()]
        nums_you_have = [int(num) for num in card.split(":")[1].split("|")[1].split()]
        card_points = 0
        for i, match in enumerate(common_numbers(winning_nums, nums_you_have)):
            if i == 0:
                card_points = 1
            else:
                card_points *= 2
        total_points += card_points
    return total_points


def common_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_nums = set1.intersection(set2)
    return list(common_nums)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("Please provide a file")
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(do_the_thing(input))
    else:
        raise TypeError("This is not a file")
