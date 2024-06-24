import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def main():
    sx, sy = NMI()
    tx, ty = NMI()
    if sy >= ty:
        sx, sy, tx, ty = tx, ty, sx, sy
    y = ty - sy
    if sy % 2 == 0:
        if sx % 2 == 0:
            l = sx - y
            r = sx + 1 + y
        else:
            l = sx - 1 - y
            r = sx + y
        if l <= tx <= r:
            print(y)
        else:
            if tx > r:
                if ty % 2 == 0 and tx % 2 == 0:
                    tx += 1
                if ty % 2 == 1 and tx % 2 == 1:
                    tx += 1
                print(y + (tx - r) // 2)
            if tx < l:
                if ty % 2 == 0 and tx % 2 == 1:
                    tx -= 1
                if ty % 2 == 1 and tx % 2 == 0:
                    tx -= 1
                print(y + (l - tx) // 2)

    else:
        if sx % 2 == 1:
            l = sx - y
            r = sx + 1 + y
        else:
            l = sx - 1 - y
            r = sx + y
        if l <= tx <= r:
            print(y)
        else:
            if tx > r:
                if ty % 2 == 0 and tx % 2 == 0:
                    tx += 1
                if ty % 2 == 1 and tx % 2 == 1:
                    tx += 1
                print(y + (tx - r) // 2)
            if tx < l:
                if ty % 2 == 0 and tx % 2 == 1:
                    tx -= 1
                if ty % 2 == 1 and tx % 2 == 0:
                    tx -= 1
                print(y + (l - tx) // 2)


if __name__ == "__main__":
    main()
