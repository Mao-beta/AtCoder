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
    A = [SI() for _ in range(N)]
    B = [["0"]*N for _ in range(N)]
    for h in range(N):
        for w in range(N):
            ah, aw = h, w
            if h == 0 and w > 0:
                aw -= 1
            elif w == N-1 and h > 0:
                ah -= 1
            elif h == N-1 and w < N-1:
                aw += 1
            elif w == 0 and h < N-1:
                ah += 1
            B[h][w] = A[ah][aw]
    for row in B:
        print("".join(row))


if __name__ == "__main__":
    main()
