"""
Advent of Code 2025 - Day 4
"""


def part1(input_data, remove=False):
    """Solve part 1 of the puzzle."""

    adjacent_coords = [
        (0, -1),
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (-1, 0),
        (-1, 1),
        (-1, -1),
    ]

    accesible_rolls = 0
    cols = len(input_data[0])
    rows = len(input_data)

    for x in range(rows):
        for y in range(cols):
            if input_data[x][y] == "@":
                count = 0
                for dx, dy in adjacent_coords:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if input_data[nx][ny] == "@":
                            count += 1
                if count < 4:
                    accesible_rolls += 1
                    if remove:
                        if remove:
                            input_data[x] = (
                                input_data[x][:y] + "." + input_data[x][y + 1 :]
                            )

    return accesible_rolls, input_data


def part2(input_data):
    """Solve part 2 of the puzzle."""

    removed_papers = 0
    count = 1
    while count > 0:
        count, input_data = part1(input_data, remove=True)
        removed_papers += count

    return removed_papers


def main():
    # Read input
    with open("day04/input.txt", "r") as f:
        input_data = f.read().strip().split("\n")

    # Solve
    result1, _ = part1(input_data)
    result2 = part2(input_data)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
