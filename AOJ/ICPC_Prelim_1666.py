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
    while True:
        N = NI()
        if N == 0:
            break
        A = EI(N)

        B = [[0]*N for _ in range(N)]
        bh, bw = 0, 0
        for h in range(N):
            s = h % 2
            for w in range(s, N, 2):
                B[bh][bw] = A[h][w]
                bw += 1
                if bw >= N:
                    bw -= N
                    bh += 1
        
        for h in range(N):
            s = h % 2
            for w in range((s+1)%2, N, 2):
                B[bh][bw] = A[h][w]
                bw += 1
                if bw >= N:
                    bw -= N
                    bh += 1

        for row in B:
            print(*row)


if __name__ == "__main__":
    main()
