import sys
import math
from collections import deque
from itertools import permutations

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    X, Y, A, B, C = NMI()

    def place(x, y, z1, z2, z3, is_x1, is_x2):
        if is_x1:
            d = (z1 + x - 1) // x
            if d >= y:
                return False
            y -= d

            if is_x2:
                d = (z2 + x - 1) // x
                if d >= y:
                    return False
                y -= d

            else:
                d = (z2 + y - 1) // y
                if d >= x:
                    return False
                x -= d

            if x * y < z3:
                return False

        else:
            d = (z1 + y - 1) // y
            if d >= x:
                return False
            x -= d

            if is_x2:
                d = (z2 + x - 1) // x
                if d >= y:
                    return False
                y -= d

            else:
                d = (z2 + y - 1) // y
                if d >= x:
                    return False
                x -= d

            if x * y < z3:
                return False

        return True


    for a, b, c in permutations([A, B, C], 3):
        for is_x1 in range(2):
            for is_x2 in range(2):
                if place(X, Y, a, b, c, is_x1, is_x2):
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
