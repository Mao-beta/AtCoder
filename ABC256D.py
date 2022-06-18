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
    LR = [NLI() for _ in range(N)]
    LR.sort()
    LR.append([10**6, 10**6])
    now_r = 0
    now_l = LR[0][0]
    ans = []
    for l, r in LR:
        if now_r < l:
            ans.append([now_l, now_r])
            now_l = l
        now_r = max(now_r, r)

    for l, r in ans[1:]:
        print(l, r)


if __name__ == "__main__":
    main()
