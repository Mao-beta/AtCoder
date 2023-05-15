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


def main():
    S = SI()
    N = NI()
    x = 0
    for i, s in enumerate(S[::-1]):
        if s == "1":
            x += 1 << i

    if x > N:
        print(-1)
        return

    for i in range(len(S)):
        k = len(S) - 1 - i
        if S[i] == "?" and x + (1 << k) <= N:
            x += 1 << k

    print(x)


if __name__ == "__main__":
    main()
