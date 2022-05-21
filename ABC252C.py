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
    N = NI()
    S = [SI() for _ in range(N)]

    ans = 10**10

    for target in range(10):
        target = str(target)
        C = [0] * 10
        for s in S:
            t = s.index(target)
            C[t] += 1
        tmp = 0
        for t, c in enumerate(C):
            if c == 0:
                continue
            tmp = max(tmp, (c-1)*10 + t)
        ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
