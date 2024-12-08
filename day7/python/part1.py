import sys
import math
from pprint import pprint


def is_solvable(goal, cur, remaining):
    if cur > goal:
        return False

    if cur == goal and len(remaining) == 0:
        return True

    if len(remaining) == 0:
        return False

    next_value = remaining[0]
    next_remaining = remaining[1:]

    return is_solvable(goal, cur + next_value, next_remaining) or is_solvable(
        goal, cur * next_value, next_remaining
    )


def main():
    records = []
    for line in (y for y in (x.strip() for x in sys.stdin) if y):
        svalue, rest = line.split(":")
        values = [int(x.strip()) for x in rest.split()]
        records.append((int(svalue), values))

    pprint(records)

    total = 0
    for goal, values in records:
        if is_solvable(goal, values[0], values[1:]):
            total += goal
            print(f"  TRUE {goal} and {values}")
        else:
            print(f"  FALSE {goal} and {values}")

    print(total)


if __name__ == "__main__":
    main()
