# -*- coding: utf-8 -*-
def function():
    pupils_num = int(input())
    pupils_heights = [int(x) for x in input().split()][:pupils_num]

    wrong_odds = []
    wrong_evens = []

    for i in range(len(pupils_heights)):
        if  (i + 1) % 2 == 0 and pupils_heights[i] % 2 != 0:
            wrong_evens.append(pupils_heights[i])
        elif  (i + 1) % 2 != 0 and pupils_heights[i] % 2 == 0:
            wrong_odds.append(pupils_heights[i])

    predicts = [
        wrong_evens == [],
        wrong_odds == [],
        len(wrong_odds) > 1,
        len(wrong_evens) > 1,
    ]

    for predict in predicts:
        if predict:
            return "-1 -1"

    return "{0} {1}".format(wrong_evens[0], wrong_odds[0])


if __name__ == "__main__":
    print(function())
