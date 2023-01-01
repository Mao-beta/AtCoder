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
    X = [NLI() for _ in range(4)]
    for row in X:
        row.sort()

    INF = 10**15
    ans = INF
    for i in range(4):
        for x in X[i]:
            tmp = 0
            for ni in range(4):
                if i == ni: continue
                idx = bisect.bisect_left(X[ni], x)
                if idx == N:
                    tmp = INF
                    break
                tmp = max(tmp, X[ni][idx] - x)
            ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
