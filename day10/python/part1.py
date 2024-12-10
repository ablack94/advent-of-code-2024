import sys
import math

def get_neighbors(x, y, grid):
    up = (x, y - 1)
    down = (x, y + 1)
    left = (x - 1, y)
    right = (x + 1, y)
    
    neighbors = []

    value = grid[(x, y)]
    for pos in (x for x in [up, down, left, right] if x in grid):
        delta = grid[pos] - value
        if delta == 1:
            neighbors.append(pos)
    
    return neighbors


def score_trailhead(x, y, grid):
    value = grid[(x, y)]
    if value == 9:
        return {(x, y)}
    
    neighbors = get_neighbors(x, y, grid)
    goals = set()
    for (nx, ny) in neighbors:
        goals.update(score_trailhead(nx, ny, grid))

    return goals


def main():
    grid = {}
    lines = (y for y in (x.strip() for x in sys.stdin) if y)
    zeros = []
    for row_num, line in enumerate(lines):
        for col_num, sval in enumerate(line):
            val = int(sval)
            pos = (col_num, row_num)
            grid[pos] = val
            if val == 0:
                zeros.append(pos)

    total = 0
    for (x, y) in zeros:
        total += len(score_trailhead(x, y, grid))
    
    print(total)


if __name__ == "__main__":
    main()

