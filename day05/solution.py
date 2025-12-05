"""
Advent of Code 2025 - Day 5
"""


def part1(ranges, all_ingredients):
    """Solve part 1 of the puzzle."""

    fresh = []
    for ingredient in all_ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                fresh.append(ingredient)
                continue

    return len(set(fresh))


def part2(ranges, all_ingredients):
    """Solve part 2 of the puzzle."""
    # sort ranges
    ranges = sorted(ranges, key=lambda x: x[0])

    merged = []
    for start, end in ranges:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    total = 0
    for start, end in merged:
        total += end - start + 1
    return total


def main():
    # Read input
    with open("day05/input.txt", "r") as f:
        input_data = f.read().strip().split("\n")
        fresh_ranges = []
        ingredients = []
        for d in input_data:
            d = d.strip()
            if "-" in d:
                start, end = d.split("-")
                fresh_ranges.append((int(start), int(end)))
            elif d == "":
                continue
            else:
                ingredients.append(int(d))

    # Solve
    result1 = part1(fresh_ranges, ingredients)
    result2 = part2(fresh_ranges, ingredients)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
