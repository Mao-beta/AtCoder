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
    Q = NI()

    C = Counter([])
    S = set()

    MAX = []
    MIN = []

    for _ in range(Q):
        query = NLI()
        t = query[0]
        if t == 1:
            x = query[1]
            C[x] += 1
            S.add(x)
            heappush(MAX, -x)
            heappush(MIN, x)

        elif t == 2:
            x, c = query[1], query[2]
            cc = C[x]
            if cc > c:
                C[x] -= c
            else:
                C[x] = 0
                S.discard(x)

        else:
            while C[-MAX[0]] <= 0:
                heappop(MAX)
            while C[MIN[0]] <= 0:
                heappop(MIN)

            print(-MAX[0] - MIN[0])


if __name__ == "__main__":
    main()
