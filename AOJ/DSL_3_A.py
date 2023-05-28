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
    N, S = NMI()
    A = NLI()
    INF = 10**10
    ans = INF
    D = deque()
    now = 0
    for a in A:
        D.append(a)
        now += a

        while D and now - D[0] >= S:
            now -= D[0]
            D.popleft()

        if now >= S:
            ans = min(ans, len(D))

    if ans == INF:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
