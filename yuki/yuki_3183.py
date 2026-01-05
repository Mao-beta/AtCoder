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
    N = NI()
    P = deque(NLI())
    ans = []
    for _ in range(15000):
        if P[0] < N-1 and P[0] > P[1]:
            ans.append("S")
            P[0], P[1] = P[1], P[0]
        else:
            ans.append("R")
            P.rotate(-1)
    while P[0] > 0:
        ans.append("R")
        P.rotate(-1)
    print("".join(ans))


if __name__ == "__main__":
    main()
