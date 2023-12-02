import sys
from pathlib import Path
import re


def do_the_thing(input):
    sum = 0
    for line in input:
        # find all digits and words that are numbers
        matches = re.findall(
            r"(\d|(?=(one|two|three|four|five|six|seven|eight|nine)))",
            line,
        )
        # flatten list of tuples
        digits = [value for tuple in matches for value in tuple if value != ""]
        first_digit = digits[0]
        last_digit = digits[-1]

        integer_from_word = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

        # convert words to digits (still strings)
        if first_digit in integer_from_word.keys():
            first_digit = integer_from_word[first_digit]
        if last_digit in integer_from_word.keys():
            last_digit = integer_from_word[last_digit]

        # concatenate first and last digit to form a two-digit number
        final_num = first_digit + last_digit
        sum += int(final_num)
    return sum


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("Please provide a file")
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(do_the_thing(input))
    else:
        raise TypeError("This is not a file")
