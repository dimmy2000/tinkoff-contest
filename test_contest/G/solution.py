# -*- coding: utf-8 -*-
def function():
    # input
    pupils_num = int(input())
    santa_little_helpers = [int(x) for x in input().split()][:pupils_num]

    # list of pupils IDs
    pupils_list = [pupil for pupil in range(1, pupils_num + 1)]

    # preparing data for comparison
    right_order = [pup + 2 if pup != pupils_num - 1 else 1 for pup in range(pupils_num)]
    santa_little_helpers.append(santa_little_helpers.pop(0))
    expected = list(zip(pupils_list, right_order))
    given = list(zip(pupils_list, santa_little_helpers))

    diff = [(given[i][0], expected[i][1]) for i in range(pupils_num) if given[i] != expected[i]]

    if not diff:
        return "-1 -1"
    return "{0} {1}".format(diff[0][0], diff[0][1])


if __name__ == "__main__":
    print(function())
