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
    N = SI()
    ans = 0
    for r in range(1, len(N)//2+1):
        for P in permutations(range(len(N)), r):
            P = set(P)
            Q = set(range(len(N))) - set(P)
            P = [N[i] for i in P]
            Q = [N[i] for i in Q]
            P.sort(reverse=True)
            Q.sort(reverse=True)
            P = int("".join(P))
            Q = int("".join(Q))
            ans = max(ans, P * Q)
    print(ans)


if __name__ == "__main__":
    main()
