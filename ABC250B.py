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
    N, A, B = NMI()
    ans = [["."]*(N*B) for _ in range(N*A)]

    for h in range(N*A):
        for w in range(N*B):
            c = 0
            if h % (2*A) >= A:
                c = 1 - c
            if w % (2*B) >= B:
                c = 1 - c
            ans[h][w] = ".#"[c]

    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
