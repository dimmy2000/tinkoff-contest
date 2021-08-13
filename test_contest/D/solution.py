# -*- coding: utf-8 -*-
def function():
    n, k = (int(num) for num in input().split())
    numbers = [int(x) for x in input().split()]

    operations = []

    for number in numbers:
        for i in range(len(str(number))):
            digit = str(number)[-(i + 1)]
            operation = 10 ** i * (9 - int(digit))
            operations.append(operation)

    operations.sort(reverse=True)
    return str(sum(operations[:k]))


if __name__ == "__main__":
    print(function())
