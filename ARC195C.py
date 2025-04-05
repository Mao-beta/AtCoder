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


def solve(R, B):
    INF = 10**7
    if R % 2:
        print("No")
        return
    if R == 0:
        if B % 2:
            print("No")
            return
        else:
            print("Yes")
            x, y = INF, INF
            for i in range(B//2):
                x += 1
                y -= 1
                print("B", x, y)
            x -= 1
            y -= 1
            for i in range(B//2):
                print("B", x, y)
                x -= 1
                y += 1
            return
    else:
        print("Yes")
        if B % 2:
            x, y = INF, INF
            print("B", x, y)
            for i in range(B//2):
                x -= 1
                y -= 1
                print("B", x, y)
            x -= 1
            y += 1
            for i in range(B//2):
                print("B", x, y)
                x += 1
                y += 1
            print("R", x, y)
            for i in range(R//2-1):
                y += 1
                print("R", x, y)
            x += 1
            print("R", x, y)
            for i in range(R//2-1):
                y -= 1
                print("R", x, y)
            return
        else:
            x, y = INF, INF
            print("R", x, y)
            for i in range(R // 2 - 1):
                y += 1
                print("R", x, y)
            x += 1
            print("R", x, y)
            for i in range(R // 2 - 1):
                y -= 1
                print("R", x, y)
            x += 1
            if B == 0:
                return
            print("B", x, y)
            for i in range(B//2-1):
                x += 1
                y -= 1
                print("B", x, y)
            x -= 1
            y -= 1
            print("B", x, y)
            for i in range(B//2-1):
                x -= 1
                y += 1
                print("B", x, y)
            return


def main():
    T = NI()
    for _ in range(T):
        R, B = NMI()
        solve(R, B)


if __name__ == "__main__":
    main()
