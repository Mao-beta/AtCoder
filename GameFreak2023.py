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


def solve1(N, X, Y, AB):
    # X == 1, Y == 1
    ans = 0
    for a, b in AB:
        ans += b - a
    print(ans)


def solve2(N, X, Y, AB):
    # Y == N
    T = [-(b - a) for a, b in AB]
    heapify(T)
    ans = 10 ** 9
    now = 0

    while True:
        M = -heappop(T)
        m = -heappop(T)
        # print(M, m)

        if M <= 0:
            break

        ans = min(ans, now + M)
        gap = M - m
        if gap == 0:
            k = 1
        else:
            k = (gap + X - 1) // X
        M -= X * k
        now += k
        if M < 0:
            M = 0

        heappush(T, -M)
        heappush(T, -m)

    print(ans)


def solve3(N, X, Y, AB):
    pass


def main():
    step = NI()
    N, X, Y = NMI()
    AB = EI(N)

    if step == 1:
        solve1(N, X, Y, AB)
    elif step == 2:
        solve2(N, X, Y, AB)
    else:
        solve3(N, X, Y, AB)


if __name__ == "__main__":
    main()
