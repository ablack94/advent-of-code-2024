from __future__ import annotations

import math
import sys
import re
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Velocity = namedtuple("Velocity", ["x", "y"])

def step(pos: Point, velocity: Velocity, size: Point):
    next_pos = Point(
        (pos.x + velocity.x) % size.x,
        (pos.y + velocity.y) % size.y,
    )
    return next_pos

def make_grid(positions: list[Point], size: Point):
    grid = [
        ['.'] * size.x
        for _ in range(0, size.y)
    ]
    for pos in positions:
        grid[pos.y][pos.x] = '*'

    return grid

def print_grid(positions: list[Point], size: Point):
    grid = make_grid(positions, size)
    for y in range(0, size.y):
        print(''.join(grid[y]))

def is_grid_mostly_symmetric(grid):
    width = len(grid[0]) // 2
    pairs = [(row[0:width], row[width:][::-1]) for row in grid]
    deltas = 0
    for lhs, rhs in pairs:
        for v1, v2 in zip(lhs, rhs):
            if v1 != v2:
                deltas += 1
    
    max_deltas = 500
    pct = 1 - (deltas / max_deltas)
    return (pct >= 0.9, pct)


def simulate(robots, size: Point):
    velocities = [velocity for (_, velocity) in robots]
    positions = [pos for (pos, _) in robots]

    steps = 0
    while True:
        for idx in range(0, len(positions)):
            positions[idx] = step(positions[idx], velocities[idx], size)
        steps += 1
        
        grid = make_grid(positions, size)
        is_symmetric, pct_same = is_grid_mostly_symmetric(grid)

        if steps % 100 == 0:
            print(steps, is_symmetric, pct_same)

        if pct_same >= 0.31:
            break


    print_grid(positions, size)

    return steps


def main():
    robots = []
    for line in (y for y in (x.strip() for x in sys.stdin) if y):
        parts = line.split()
        px, py = [int(x) for x in parts[0].split("=")[1].split(",")]
        vx, vy = [int(x) for x in parts[1].split("=")[1].split(",")]
        robots.append((Point(px, py), Velocity(vx, vy)))

    dimensions = Point(101, 103)

    print(simulate(robots, dimensions))


if __name__ == "__main__":
    main()
