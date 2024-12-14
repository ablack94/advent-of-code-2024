from __future__ import annotations

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

def print_grid(positions: list[Point], size: Point):
    grid = [
        ['.'] * size.x
        for _ in range(0, size.y)
    ]
    for pos in positions:
        grid[pos.y][pos.x] = '*'
    
    for y in range(0, size.y):
        print(''.join(grid[y]))

def simulate(robots, size: Point):
    velocities = [velocity for (_, velocity) in robots]
    positions = [pos for (pos, _) in robots]

    steps = 0
    while True:
        for idx in range(0, len(positions)):
            positions[idx] = step(positions[idx], velocities[idx], size)
        steps += 1
        
        upos = set(positions)
        if len(positions) == len(upos):
            break

    print_grid(positions, size)

    return steps

def count_by_quadrant(positions: list[Point], size: Point):
    cx, cy = size.x // 2, size.y // 2
    quads = {}
    for pos in positions:
        if pos.x == cx or pos.y == cy:
            continue
        else:
            key = (pos.x < cx, pos.y < cy)
            quads[key] = quads.setdefault(key, 0) + 1

    from functools import reduce
    return reduce(lambda x, y: x * y, quads.values())



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
