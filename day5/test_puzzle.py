from pathlib import Path
import pytest
from puzzle import do_the_thing

file = Path("test_input.txt")
input = Path.read_text(file).splitlines()
expected_output = 35


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (input, expected_output),
    ],
)
def test_do_the_thing(input, expected_output):
    assert do_the_thing(input) == expected_output
