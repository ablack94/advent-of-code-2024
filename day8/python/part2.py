import sys
from pprint import pprint


def calculate_antinodes(a1, a2, grid):
    x1, y1 = a1
    x2, y2 = a2

    dy = y2 - y1
    dx = x2 - x1

    nodes = set()

    x, y = (x1, y1)
    while True:
        node = (x, y)
        if node in grid:
            nodes.add(node)
            x, y = ((x + dx), (y + dy))
        else:
            break

    x, y = (x1, y1)
    while True:
        node = (x, y)
        if node in grid:
            nodes.add(node)
            x, y = ((x - dx), (y - dy))
        else:
            break

    return nodes


def main():
    ants = {}
    grid = set()
    grid_width = float("-inf")
    grid_height = float("inf")
    for row_num, line in enumerate((y for y in (x.strip() for x in sys.stdin) if y)):
        grid_height = max(grid_height, row_num)
        for col_num, char in enumerate(line):
            grid_width = max(grid_width, col_num)
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

                antinodes.update(calculate_antinodes(a1, a2, grid))

    pprint(antinodes)
    va = [x for x in antinodes if x in grid]
    pprint(va)
    print(len(va))


if __name__ == "__main__":
    main()
