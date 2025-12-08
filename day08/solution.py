"""
Advent of Code 2025 - Day 8
"""


def distance(point1, point2):
    return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5


def part1(input_data, steps: int = 1000):
    """Solve part 1 of the puzzle."""
    closest_pairs = []

    for i in range(len(input_data)):
        for j in range(i + 1, len(input_data)):
            dist = distance(input_data[i], input_data[j])
            closest_pairs.append((input_data[i], input_data[j], dist))

    closest_pairs.sort(key=lambda x: x[2])
    circuits = []

    for pair_idx in range(steps):
        point1, point2 = closest_pairs[pair_idx][:2]
        pair_set = {point1, point2}

        intersecting_indices = [
            idx for idx, circ in enumerate(circuits) if circ & pair_set
        ]

        if len(intersecting_indices) == 0:
            # Case 1 - both points are not in any circuit - create new circuit
            circuits.append(pair_set)
        elif len(intersecting_indices) == 1:
            # Case 2 - one or both points already in a circuit - add to it
            circuits[intersecting_indices[0]] |= pair_set
        else:
            # Case 3- points are in different circuits - merge all intersecting circuits
            merged = pair_set.copy()
            for idx in intersecting_indices:
                merged |= circuits[idx]
            # remove old circuits and add merged one
            circuits = [
                circ
                for idx, circ in enumerate(circuits)
                if idx not in intersecting_indices
            ]
            circuits.append(merged)

    all_points = set(input_data)
    connected_points = set(p for circuit in circuits for p in circuit)
    for point in all_points - connected_points:
        circuits.append({point})

    # Result is the multiplication of largest 3 circuit sizes
    circuit_sizes = sorted([len(c) for c in circuits], reverse=True)[:3]

    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


def part2(input_data):
    """Solve part 2 of the puzzle."""
    closest_pairs = []

    for i in range(len(input_data)):
        for j in range(i + 1, len(input_data)):
            dist = distance(input_data[i], input_data[j])
            closest_pairs.append((input_data[i], input_data[j], dist))

    closest_pairs.sort(key=lambda x: x[2])
    circuits = []

    for point1, point2, _ in closest_pairs:
        pair_set = {point1, point2}

        intersecting_indices = [
            idx for idx, circ in enumerate(circuits) if circ & pair_set
        ]

        if len(intersecting_indices) == 0:
            circuits.append(pair_set)
        elif len(intersecting_indices) == 1:
            circuits[intersecting_indices[0]] |= pair_set
        else:
            merged = pair_set.copy()
            for idx in intersecting_indices:
                merged |= circuits[idx]
            circuits = [
                circ
                for idx, circ in enumerate(circuits)
                if idx not in intersecting_indices
            ]
            circuits.append(merged)

        # Check if all points are now in a single circuit
        if len(circuits) == 1 and len(circuits[0]) == len(input_data):
            print("All junction boxes connected!")
            print(f"Last connection: {point1} and {point2}")
            print(f"X coordinates: {point1[0]} and {point2[0]}")
            result = point1[0] * point2[0]
            print(f"Result: {result}")
            return result

    return None


def main():
    # Read input
    with open("day08/input.txt", "r") as f:
        input_data = [tuple(int(x) for x in line.strip().split(",")) for line in f]

    # Solve
    result1 = part1(input_data)
    result2 = part2(input_data)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
