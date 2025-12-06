"""
Advent of Code 2025 - Day 6
"""
import math


def part1(input_data):
    """Solve part 1 of the puzzle."""

    cleaned_input_data = []
    for i, d in enumerate(input_data):
        if i < len(input_data) - 1:
            parts = [int(x) for x in d.split() if x.strip()]
            cleaned_input_data.append(parts)
        else:
            parts = [x for x in d.split() if x.strip()]
            cleaned_input_data.append(parts)

    signs = cleaned_input_data[-1]

    total = 0
    for i, sign in enumerate(signs):
        a, b, c, d = (
            cleaned_input_data[0][i],
            cleaned_input_data[1][i],
            cleaned_input_data[2][i],
            cleaned_input_data[3][i],
        )

        if sign == "+":
            total += a + b + c + d
        elif sign == "*":
            total += a * b * c * d

    return total


def part2(input_data):
    """Solve part 2 of the puzzle."""
    signs = input_data[-1]
    current_char = None
    num_list = []
    total = 0

    for i, char in enumerate(signs):
        num = "".join(
            [
                input_data[0][i],
                input_data[1][i],
                input_data[2][i],
                input_data[3][i],
            ]
        ).strip()

        if char in ("+", "*"):
            current_char = char
            num_list = [int(num)]
        else:
            if num:
                num_list.append(int(num))
            else:
                if current_char == "+":
                    total += sum(num_list)
                elif current_char == "*":
                    total += math.prod(num_list)
                num_list = []

        if i == len(signs) - 1:
            if current_char == "+":
                total += sum(num_list)
            elif current_char == "*":
                total += math.prod(num_list)

    return total


def main():
    # Read input
    with open("day06/input.txt", "r") as f:
        input_data = f.read().split("\n")

    # Solve
    result1 = part1(input_data)
    result2 = part2(input_data)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
