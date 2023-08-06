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
    RC = EI(N-1)
    B = [[1]*N for _ in range(N)]
    RC = [[x-1, y-1] for x, y in RC]

    for qr, qc in RC:
        for i in range(N):
            B[i][qc] = 0
            B[qr][i] = 0

        for i in range(-N, N + 1):
            nr, nc = qr + i, qc + i
            if 0 <= nr < N and 0 <= nc < N:
                B[nr][nc] = 0
            nr, nc = qr + i, qc - i
            if 0 <= nr < N and 0 <= nc < N:
                B[nr][nc] = 0

    for r in range(N):
        for c in range(N):
            if B[r][c]:
                print(r+1, c+1)
                exit()

    print(-1)


if __name__ == "__main__":
    main()
