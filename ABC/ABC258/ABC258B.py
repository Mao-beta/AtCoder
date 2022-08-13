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
    A = [list(map(int, list(SI()))) for _ in range(N)]
    ans = 0
    DH = [0, 0, -1, 1, 1, 1, -1, -1]
    DW = [1, -1, 0, 0, 1, -1, 1, -1]
    for h in range(N):
        for w in range(N):
            for dh, dw in zip(DH, DW):
                tmp = 0
                nh = h
                nw = w
                for i in range(N):
                    tmp = tmp * 10 + A[nh%N][nw%N]
                    nh += dh
                    nw += dw
                ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
