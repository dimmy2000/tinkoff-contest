# -*- coding: utf-8 -*-
def function():
    a, b, c, d = [int(x) for x in input().split()]
    if d - b > 0:
        return str(a + (d - b) * c)
    else:
        return str(a)

if __name__ == "__main__":
    print(function())
