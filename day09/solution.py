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
        x1, y1 = input_data[i]
        x2, y2 = input_data[(i + 1) % n]

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                perimeter.add((x, y1))
        else:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                perimeter.add((x1, y))

    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = input_data[i]
            x2, y2 = input_data[j]

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            if area <= max_area:
                continue

            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)

            # Check if any perimeter point is strictly inside the rectangle
            found_conflict = False
            for px, py in perimeter:
                if min_x < px < max_x and min_y < py < max_y:
                    found_conflict = True
                    break

            # Rectangle is valid if no perimeter points are strictly inside
            if not found_conflict:
                max_area = area

    return max_area


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
