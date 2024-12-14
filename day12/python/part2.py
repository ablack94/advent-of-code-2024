import sys
from pprint import pprint
from attr import define, field


def get_neighbors(pos):
    p_up = (pos[0], pos[1] - 1)
    p_down = (pos[0], pos[1] + 1)
    p_left = (pos[0] - 1, pos[1])
    p_right = (pos[0] + 1, pos[1])
    return (p_up, p_down, p_left, p_right)


def filter_to_same_neighbors(label, neighbors, graph):
    return [pos if graph.get(pos) == label else None for pos in neighbors]


def count_corners(pos, graph):
    label = graph[pos]
    ul = graph.get((pos[0] - 1, pos[1] - 1)) == label
    up = graph.get((pos[0], pos[1] - 1)) == label
    ur = graph.get((pos[0] + 1, pos[1] - 1)) == label
    left = graph.get((pos[0] - 1, pos[1])) == label
    right = graph.get((pos[0] + 1, pos[1])) == label
    dl = graph.get((pos[0] - 1, pos[1] + 1)) == label
    down = graph.get((pos[0], pos[1] + 1)) == label
    dr = graph.get((pos[0] + 1, pos[1] + 1)) == label

    conditions = [
        not (up or left),
        not (up or right),
        not (down or left),
        not (down or right),
        left and not ul and up,
        right and not ur and up,
        left and not dl and down,
        right and not dr and down,
    ]

    return sum([1 if x is True else 0 for x in conditions])


def evaluate(graph):
    visited = set()

    def flood(pos):
        if pos in visited:
            return None

        visited.add(pos)

        label = graph[pos]
        neighbors = get_neighbors(pos)
        nvalues = [graph.get(x) for x in neighbors]
        perimeter = sum([1 if x == label else 0 for x in nvalues])
        corners = count_corners(pos, graph)
        area = 1

        for npos, nvalue in zip(neighbors, nvalues):
            if nvalue == label:
                result = flood(npos)
                if result is not None:
                    other_perimeter, other_corners, other_area = result
                    perimeter += other_perimeter
                    corners += other_corners
                    area += other_area

        return (perimeter, corners, area)

    total = 0

    for pos in graph:
        result = flood(pos)
        if result is not None:
            perimeter, corners, area = result
            print(corners, area, corners * area)
            total += corners * area

    return total


def main():

    walls = {}
    grid = {}
    lines = (y for y in (x.strip() for x in sys.stdin) if y)
    for y, line in enumerate(lines):
        for x, label in enumerate(line):
            grid[(x, y)] = label

    print(evaluate(grid))


if __name__ == "__main__":
    main()
