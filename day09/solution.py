"""
Advent of Code 2025 - Day 9
"""


def part1(input_data):
    """Solve part 1 of the puzzle."""

    max_area = 0

    for i in range(len(input_data)):
        for j in range(i + 1, len(input_data)):
            area = abs(input_data[i][0] - input_data[j][0] + 1) * abs(
                input_data[i][1] - input_data[j][1] + 1
            )
            if area > max_area:
                max_area = area

    return max_area


def part2(input_data):
    """Solve part 2 of the puzzle."""

    n = len(input_data)
    areas = []

    for i in range(n):
        for j in range(i + 1, n):
            area = abs(input_data[i][0] - input_data[j][0] + 1) * abs(
                input_data[i][1] - input_data[j][1] + 1
            )
            areas.append([area, (i, j)])

    areas.sort(reverse=True)

    perimeter = set()

    for i in range(n):
        x1, y1 = input_data[i - 1]
        x2, y2 = input_data[i]

        if x1 == x2:  # vertical edge
            for y in range(min(y1, y2), max(y1, y2) + 1):
                perimeter.add((x1, y))

        elif y1 == y2:  # horizontal edge
            for x in range(min(x1, x2), max(x1, x2) + 1):
                perimeter.add((x, y1))

    result = 0

    for area, (i, j) in areas:
        x_min = min(input_data[i][0], input_data[j][0])
        x_max = max(input_data[i][0], input_data[j][0])
        y_min = min(input_data[i][1], input_data[j][1])
        y_max = max(input_data[i][1], input_data[j][1])

        bad = False
        for x, y in perimeter:
            if x_min < x < x_max and y_min < y < y_max:
                bad = True
                break

        if bad:
            continue

        result = area
        break

    return result


def main():
    # Read input
    with open("day09/input.txt", "r") as f:
        input_data = [tuple(int(x) for x in line.split(",")) for line in f]

    # Solve
    result1 = part1(input_data)
    result2 = part2(input_data)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
