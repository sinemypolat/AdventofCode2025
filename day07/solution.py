"""
Advent of Code 2025 - Day 7
"""


def part1(input_data):
    """Solve part 1 of the puzzle."""
    start = ()
    rows = len(input_data)
    cols = len(input_data[0])

    # find the start letter 'S'
    for r in range(rows):
        for c in range(cols):
            if input_data[r][c] == 'S':
                start = (r, c)

    # beams: list of (row, col)
    beams = [(start[0] + 1, start[1])]  # now start moving downward
    visited = set()
    splits = 0

    while beams:
        r, c = beams.pop()

        # out of bounds
        if not (0 <= r < rows and 0 <= c < cols):
            continue

        # avoid reprocessing same cell
        if (r, c) in visited:
            continue
        visited.add((r, c))

        cell = input_data[r][c]

        if cell == '.':
            beams.append((r + 1, c))

        elif cell == '^':
            splits += 1
            # spawn left and right beams
            beams.append((r, c - 1))
            beams.append((r, c + 1))
        elif cell == 'S':
            beams.append((r + 1, c))

    return splits


def part2(input_data):
    """Solve part 2 of the puzzle."""
    from collections import deque

    rows, cols = len(input_data), len(input_data[0])

    # find the start letter 'S'
    start = None
    for r in range(rows):
        for c in range(cols):
            if input_data[r][c] == 'S':
                start = (r, c)
                break
        if start:
            break

    if not start:
        return 0

    ways = [[0] * cols for _ in range(rows + 1)]
    sr, sc = start
    seed_row = min(sr + 1, rows)
    ways[seed_row][sc] += 1

    for r in range(seed_row, rows + 1):
        if r == rows:
            continue
        curr = ways[r][:]
        ways[r] = [0] * cols
        dq = deque([c for c, v in enumerate(curr) if v > 0])
        while dq:
            c = dq.popleft()
            v = curr[c]
            if v == 0:
                continue
            curr[c] = 0
            cell = input_data[r][c]
            if cell == '.':
                ways[r + 1][c] += v
            elif cell == '^':
                if c - 1 >= 0:
                    was = curr[c - 1]
                    curr[c - 1] += v
                    if was == 0:
                        dq.append(c - 1)
                if c + 1 < cols:
                    was = curr[c + 1]
                    curr[c + 1] += v
                    if was == 0:
                        dq.append(c + 1)
            elif cell == 'S':
                ways[r + 1][c] += v

    total = sum(ways[rows][c] for c in range(cols))
    return total


def main():
    # Read input
    with open("day07/input.txt", "r") as f:
        input_data = [line.strip() for line in f.readlines() if line.strip()]

    # Solve
    result1 = part1(input_data)
    result2 = part2(input_data)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
