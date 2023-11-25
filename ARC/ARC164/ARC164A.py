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


def solve(N, K):
    res = 0
    n = N
    while n > 0:
        a, r = divmod(n, 3)
        n = a
        res += r
    if res <= K and (res - K) % 2 == 0:
        return True
    else:
        return False


def main():
    T = NI()
    for _ in range(T):
        N, K = NMI()
        res = solve(N, K)
        if res:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
