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
    N, K = NMI()
    TD = [NLI() for _ in range(N)]
    TD.sort(key=lambda x: -x[1])
    used = set()
    now = 0
    hq = []
    heapify(hq)

    for i in range(K):
        t, d = TD[i]
        now += d
        if t in used:
            heappush(hq, d)

        used.add(t)

    k = len(used)
    ans = now + k ** 2

    for i in range(K, N):
        t, d = TD[i]
        if t in used:
            continue

        if not hq:
            break

        hd = heappop(hq)
        now -= hd
        now += d
        k += 1
        used.add(t)
        ans = max(ans, now + k ** 2)

    print(ans)


if __name__ == "__main__":
    main()
