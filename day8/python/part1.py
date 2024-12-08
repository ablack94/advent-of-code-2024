import sys
from pprint import pprint


def calculate_antinodes(a1, a2):
    x1, y1 = a1
    x2, y2 = a2

    dy = y2 - y1
    dx = x2 - x1

    n1 = ((x2 + dx), (y2 + dy))
    n2 = ((x1 - dx), (y1 - dy))

    # print(f"x1 {x1} y1 {y1}")
    # print(f"x2 {x2} y2 {y2}")
    # print(f"dx {dx} dy {dy}")
    # print(f"n1 {n1} n2 {n2}")

    return (n1, n2)


def main():
    ants = {}
    grid = set()
    for row_num, line in enumerate((y for y in (x.strip() for x in sys.stdin) if y)):
        for col_num, char in enumerate(line):
            grid.add((col_num, row_num))
            if char != ".":
                ants.setdefault(char, set()).add((col_num, row_num))

    pprint(ants)
    pprint(grid)

    antinodes = set()

    for ant, positions in ants.items():
        lps = list(positions)
        for a1 in lps:
            for a2 in lps:
                if a1 == a2:
                    continue

                n1, n2 = calculate_antinodes(a1, a2)
                antinodes.add(n1)
                antinodes.add(n2)

    pprint(antinodes)
    va = [x for x in antinodes if x in grid]
    pprint(va)
    print(len(va))


if __name__ == "__main__":
    main()
