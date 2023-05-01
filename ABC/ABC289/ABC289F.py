import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main(sx, sy, tx, ty, a, b, c, d):
    gx, gy = tx-sx, ty-sy
    ans = []

    if gx == 0 and gy == 0:
        print("Yes")
        ans = []

    elif gx % 2 or gy % 2:
        print("No")
        return None

    elif b-a == d-c == 0:
        if tx == 2*a - sx and ty == 2*c - sy:
            print("Yes")
            # print(a, c)
            ans = [[a, c]]

        else:
            print("No")
            return None

    elif b-a == 0 and d-c > 0:
        if tx == sx:
            print("Yes")
            ans = []
            y_sig = gy // abs(gy)

            for i in range(abs(gy) // 2):
                if y_sig > 0:
                    ans.append([a, c])
                    ans.append([a, c + 1])
                else:
                    ans.append([a, c + 1])
                    ans.append([a, c])

            # for row in ans:
            #     print(*row)

        elif tx == 2*a - sx:
            print("Yes")
            ans = [[a, c]]
            sy = 2*c - sy
            gy = ty - sy
            y_sig = gy // abs(gy)

            for i in range(abs(gy) // 2):
                if y_sig > 0:
                    ans.append([a, c])
                    ans.append([a, c + 1])
                else:
                    ans.append([a, c + 1])
                    ans.append([a, c])

            # for row in ans:
            #     print(*row)

        else:
            print("No")
            return None


    elif b - a > 0 and d - c == 0:
        if ty == sy:
            print("Yes")
            ans = []
            x_sig = gx // abs(gx)

            for i in range(abs(gx) // 2):
                if x_sig > 0:
                    ans.append([a, c])
                    ans.append([a + 1, c])
                else:
                    ans.append([a + 1, c])
                    ans.append([a, c])

            # for row in ans:
            #     print(*row)

        elif ty == 2 * c - sy:
            print("Yes")
            ans = [[a, c]]
            sx = 2 * a - sx
            gx = tx - sx
            x_sig = gx // abs(gx)

            for i in range(abs(gx) // 2):
                if x_sig > 0:
                    ans.append([a, c])
                    ans.append([a + 1, c])
                else:
                    ans.append([a + 1, c])
                    ans.append([a, c])

            # for row in ans:
            #     print(*row)

        else:
            print("No")
            return None

    else:
        print("Yes")
        ans = []
        x_sig = gx // abs(gx)
        y_sig = gy // abs(gy)

        for i in range(abs(gx)//2):
            if x_sig > 0:
                ans.append([a, c])
                ans.append([a+1, c])
            else:
                ans.append([a+1, c])
                ans.append([a, c])

        for i in range(abs(gy)//2):
            if y_sig > 0:
                ans.append([a, c])
                ans.append([a, c+1])
            else:
                ans.append([a, c+1])
                ans.append([a, c])

        # for row in ans:
        #     print(*row)

    return ans


def check(sx, sy, tx, ty, ans):
    x = sx
    y = sy
    for p, q in ans:
        x = 2*p - x
        y = 2*q - y

    assert len(ans) <= 10**6
    assert x == tx and y == ty


from random import randint

if __name__ == "__main__":
    sx, sy = NMI()
    tx, ty = NMI()
    a, b, c, d = NMI()

    ans = main(sx, sy, tx, ty, a, b, c, d)
    if ans is not None:
        for row in ans:
            print(*row)

    # for _ in range(1000):
    #     sx = randint(0, 200000)
    #     sy = randint(0, 200000)
    #     tx = randint(0, 200000)
    #     ty = randint(0, 200000)
    #
    #     a, b, c, d = randint(0, 200000), randint(0, 200000), randint(0, 200000), randint(0, 200000)
    #     if a > b:
    #         a, b = b, a
    #     if c > d:
    #         c, d = d, c
    #
    #     b = a
    #
    #     print(sx, sy, tx, ty, a, b, c, d)
    #     ans = main(sx, sy, tx, ty, a, b, c, d)
    #     print(ans)
    #     if ans is not None:
    #         check(sx, sy, tx, ty, ans)