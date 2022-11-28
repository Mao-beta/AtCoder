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
    A = NLI()
    ans = []
    INF = 10**15
    IA = [[i, a] for i, a in enumerate(A)]
    IA[-1][0] = INF

    rem = set(range(1, N+1)) - set(A)
    rem = sorted(list(rem))
    now_rem = 0
    for i, a in IA:
        ans.append([i, a])

        if i == INF:
            while now_rem < len(rem):
                now = rem[now_rem]
                gap = a - now
                ans.append([i+gap, now])
                now_rem += 1

        if now_rem < len(rem):
            now = rem[now_rem]
            if a < now:
                continue

            ans.append([i+0.5, now])
            now_rem += 1

    ans.sort()
    ans = [a for i, a in ans]
    print(*ans)


if __name__ == "__main__":
    main()
