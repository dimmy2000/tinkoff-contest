# -*- coding: utf-8 -*-
def function():
    """PT - Частичное решение. :("""
    employees, time_to_leave = [int(x) for x in input().split()]
    floors = [int(x) for x in input().split()]
    employee = int(input())

    deadline = floors[employee - 1]

    min_floor = floors[0]
    max_floor = floors[-1]

    if deadline - min_floor < time_to_leave:
        summary_time = max_floor - min_floor

    else:
        up = max_floor - min_floor + max_floor - deadline
        down = max_floor - min_floor + deadline - min_floor
        summary_time = min(up, down)

    return str(summary_time)


if __name__ == "__main__":
    print(function())
