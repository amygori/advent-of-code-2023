import sys
from pathlib import Path
import re


def do_the_thing(input):
    sum = 0
    for line in input:
        digits = re.findall(r"\d", line)
        sum += int(digits[0] + digits[-1])
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
