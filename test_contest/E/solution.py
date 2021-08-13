# -*- coding: utf-8 -*-
def function():
    lesser, bigger = (int(x) for x in input().split())

    digits = len(str(bigger))
    tests = []

    for k in range(1, 10):
        if digits == 1:
            if lesser <= k <= bigger:
                tests.append(k)
        else:
            for digit in range(1, digits + 1):
                test = int(str(k) * (digit))
                if lesser <= test <= bigger:
                    tests.append(test)

    tests = set(tests)
    return str(len(tests))


if __name__ == "__main__":
    print(function())
