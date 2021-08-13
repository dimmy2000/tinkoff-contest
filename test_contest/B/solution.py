# -*- coding: utf-8 -*-
def function():
    eaters = int(input())
    if eaters == 1:
        return str(0)
    else:
        counter = 0
        slices = 1
        while True:
            slices *= 2
            counter += 1
            if slices >= eaters:
                return str(counter)


if __name__ == "__main__":
    print(function())
