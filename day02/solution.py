"""
Advent of Code 2025 - Day 2
Solution template
"""


def find_invalid_numbers(input_data):
    """Solve part 1 and 2 of the puzzle."""
    pairs = [pair.split("-") for pair in input_data]

    # part 1
    invalid_ids = []
    valid_ids = []
    for start, end in pairs:
        start, end = int(start), int(end)
        for id_num in range(start, end + 1):
            str_id_num = str(id_num)
            len_id = len(str_id_num)
            mid = len_id // 2
            if len_id % 2 == 0:
                if str_id_num[0:mid] == str_id_num[mid:]:
                    invalid_ids.append(id_num)
                else:
                    valid_ids.append(id_num)
            else:
                valid_ids.append(id_num)

    # part 2
    # check valid ids again for more cases
    other_invalid_ids = []
    for id_num in valid_ids:
        str_id_num = str(id_num)
        new_num = str_id_num[1:] + str_id_num[:-1]
        if str_id_num in new_num:
            other_invalid_ids.append(id_num)

    return sum(invalid_ids), sum(invalid_ids) + sum(other_invalid_ids)


def main():
    # Read input
    with open("day02/input.txt", "r") as f:
        input_data = f.read().strip().split(",")

    # Solve
    result1, result2 = find_invalid_numbers(input_data)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
