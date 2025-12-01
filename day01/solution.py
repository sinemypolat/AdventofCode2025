"""
Advent of Code 2025 - Day 1
"""


def part1(input_data, current_location):
    """Solve part 1 of the puzzle."""
    passing_zero_times = 0

    for instruction in input_data:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == "R":
            current_location = current_location + steps

        elif direction == "L":
            current_location = current_location - steps

        current_location = current_location % 100
        if current_location == 0:
            passing_zero_times += 1

    return passing_zero_times


def part2(input_data, current_location):
    """Solve part 2 of the puzzle."""
    passing_zero_times = 0

    for instruction in input_data:
        direction = instruction[0]
        steps = int(instruction[1:])

        passing_zero_times += steps // 100
        remainder = steps % 100

        if direction == "R":
            end_location = (current_location + remainder) % 100
            if current_location + remainder >= 100:
                passing_zero_times += 1

        elif direction == "L":
            end_location = (current_location - remainder) % 100
            if current_location - remainder < 0:
                passing_zero_times += 1

        current_location = end_location

    return passing_zero_times


def main():
    # Read input
    with open("day01/input.txt", "r") as f:
        input_data = f.read().strip().split("\n")

    initial_location = 50
    # Solve
    result1 = part1(input_data, initial_location)
    result2 = part2(input_data, initial_location)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
