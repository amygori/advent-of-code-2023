import sys
from pathlib import Path


def part_two(input):
    count = len(input)
    cards_to_count = input.copy()
    while len(cards_to_count) > 0:
        card = cards_to_count.pop()
        winning_nums = [int(num) for num in card.split(":")[1].split("|")[0].split()]
        nums_you_have = [int(num) for num in card.split(":")[1].split("|")[1].split()]
        num_copies_won = len(common_numbers(winning_nums, nums_you_have))
        count += num_copies_won
        original_index = get_original_index(card)
        for i in range(num_copies_won):
            cards_to_count.append(input[original_index + 1 + i])
    return count


def get_original_index(card):
    card_number = int([card for card in card.split(":")[0].split(" ") if card][1])
    return card_number - 1


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
        print(part_two(input))
    else:
        raise TypeError("This is not a file")
