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
    N, M = NMI()
    INF = 10**20
    ans = INF
    for a in range(1, min(N+1, 10**6+1)):
        X = (M + a-1) // a * a
        if X // a > N:
            continue
        ans = min(ans, X)
    print(-1 if ans == INF else ans)


if __name__ == "__main__":
    main()
