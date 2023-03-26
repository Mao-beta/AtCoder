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
    N, M, V = NMI()

    ans = 0
    for hg in range(1, N+1):
        for wg in range(1, M+1):
            if 2*V % (hg*wg):
                continue
            X = 2*V // (hg*wg)
            p2 = X - M * (hg-1) + 1 - wg
            # print(hg, wg, p2, X)
            if p2 % 2:
                continue
            p = p2 // 2
            h, w = divmod(p-1, M)
            if h < 0 or h >= N or w < 0 or w >= M:
                continue
            if h + hg > N or w + wg > M:
                continue
            # print(h, w, hg, wg)
            v2 = hg * wg * (p*2 + wg - 1 + M * (hg-1))
            if v2 % 2 or v2 // 2 != V:
                continue
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
