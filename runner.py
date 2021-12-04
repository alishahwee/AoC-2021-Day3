from solution import part_one, part_two


def parse_puzzle_input(file: str) -> list[int]:
    """Parse the puzzle input so that each line is an element in a list.
    Then return the list."""
    with open(file) as f:
        return [int(num) for num in f]


if __name__ == "__main__":
    input = parse_puzzle_input("puzzle-input.txt")

    print(
        f"""
    Answers:
    Part one: {part_one(input)}
    Part two: {part_two(input)}
    """
    )
