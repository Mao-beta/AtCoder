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


def main():
    N = NI()
    S = [tuple(NMI()) for _ in range(N)]
    T = [tuple(NMI()) for _ in range(N)]

    if set(S) == set(T):
        print("Yes")
        exit()

    S = [[x * N, y * N] for x, y in S]
    T = [[x * N, y * N] for x, y in T]

    sx, sy = 0, 0
    tx, ty = 0, 0
    for x, y in S:
        sx += x
        sy += y
    for x, y in T:
        tx += x
        ty += y

    sx //= N
    sy //= N
    tx //= N
    ty //= N

    if sx != tx and sy != ty:
        print("No")
        exit()


    if sx != tx:
        S = [(x - sx, y) for x, y in S]
        SX = [(-x, y) for x, y in S]
        TX = set((x - tx, y) for x, y in T)

        if set(S) == TX or set(SX) == TX:
            print("Yes")
        else:
            print("No")

    else:
        S = [(x, y - sy) for x, y in S]
        SY = [(x, -y) for x, y in S]
        TY = set((x, y - ty) for x, y in T)

        if set(S) == TY or set(SY) == TY:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
