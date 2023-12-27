import sys
from pathlib import Path
import string
from collections import deque

mapping_headers = deque(
    [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
)


def do_the_thing(input):
    maps = parse_input(input)
    locations = []
    for seed in maps["seeds"]:
        copy_mapping_headers = mapping_headers.copy()
        locations.append(get_location(seed, copy_mapping_headers, maps))

    return min(locations)


def get_location(source, mappings, maps):
    mapping_header = mappings.popleft()
    for source_start, mapping in maps[mapping_header].items():
        range_length = mapping["range_length"]
        if source in range(source_start, source_start + range_length):
            dest_start = mapping["dest_start"]
            dest = dest_start + (source - source_start)
            break
        else:
            dest = source
    if len(mappings) == 0:
        return dest

    return get_location(dest, mappings, maps)


def parse_input(input):
    maps = {}
    last_heading = ""
    for index, line in enumerate(input):
        if line.startswith("seeds"):
            maps["seeds"] = [int(num) for num in line.split(":")[1].strip().split(" ")]
        elif line.endswith(":"):
            key = line.split(" ")[0]
            maps[key] = {}
            last_heading = key
        elif line.startswith(tuple(string.digits)):
            numbers = [int(num) for num in line.split(" ")]
            source_start = numbers[1]
            maps[last_heading][source_start] = {
                "dest_start": numbers[0],
                "range_length": numbers[2],
            }
        else:  # line is a blank line
            continue
    return maps


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("Please provide a file")
    file = Path(sys.argv[1])
    if Path.is_file(file):
        input = Path.read_text(file).splitlines()
        print(do_the_thing(input))
    else:
        raise TypeError("This is not a file")
