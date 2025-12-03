"""
Advent of Code 2025 - Day 3
Solution template
"""


def part1(input_data):
    """
    Solve part 1 of the puzzle.
    Find the largest joltage battery with 2 digits.
    """

    total = 0
    for line in input_data:
        batteries = [int(i) for i in line]
        first_largest_num = max(batteries[:-1])
        first_largest_num_idx = batteries.index(first_largest_num)
        second_largest_num = max(batteries[first_largest_num_idx + 1 :])
        total += (10 * first_largest_num) + second_largest_num

    return total


def part2(input_data):
    """
    Solve part 2 of the puzzle.
    Find the largest joltage battery with 12 digits.
    """
    total = 0
    for line in input_data:
        batteries = [int(i) for i in line]
        digits_to_remove = len(batteries) - 12
        result = []

        for i, num in enumerate(batteries):
            while (
                result
                and digits_to_remove > 0
                and num > result[-1]
                and len(batteries) - i > 12 - len(result)
            ):
                result.pop()
                digits_to_remove -= 1
            result.append(num)

        while len(result) > 12:
            result.pop()

        number = int("".join(map(str, result)))
        total += number

    return total


def main():
    # Read input
    with open("day03/input.txt", "r") as f:
        input_data = f.read().strip().split("\n")

    # Solve
    result1 = part1(input_data)
    result2 = part2(input_data)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
