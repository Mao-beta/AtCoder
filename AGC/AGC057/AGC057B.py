import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
import time

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
    t = time.time()
    N, X = NMI()
    A = NLI()
    max_of_min = []
    min_of_max = []

    MAX = A.copy()
    MIN = A.copy()

    for i, a in enumerate(A):
        heappush(max_of_min, (-a, i))
        heappush(min_of_max, (a, i))

    # print(max_of_min)
    # print(min_of_max)

    ans = max(A) - min(A)
    INF = (1 << 80)

    while time.time() - t < 3.7:
        # print(-max_of_min[0][0], min_of_max[0][0])
        while True:
            m, i = max_of_min[0]
            m = -m
            if m < MIN[i]:
                heappop(max_of_min)
            else:
                break

        ans = min(-max_of_min[0][0] - min_of_max[0][0], ans)
        if ans <= 0:
            print(0)
            exit()
        # print(c, ans)

        m, i = heappop(min_of_max)

        # print(m)

        if m < MIN[i]:
            continue

        MAX[i] = MAX[i] * 2 + X
        MIN[i] = MIN[i] * 2

        if MAX[i] > INF:
            break
        heappush(max_of_min, (-MIN[i], i))
        heappush(min_of_max, (MAX[i], i))

        # print(MAX)
        # print(MIN)
        # print()

    print(ans)


if __name__ == "__main__":
    main()
