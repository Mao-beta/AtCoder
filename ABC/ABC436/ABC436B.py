import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    A = [[0]*N for _ in range(N)]
    A[0][(N-1)//2] = 1
    r = 0
    c = (N-1) // 2
    for i in range(2, N**2+1):
        nr = (r-1) % N
        nc = (c+1) % N
        if A[nr][nc] == 0:
            A[nr][nc] = i
        else:
            nr = (r + 1) % N
            nc = c
            A[(r+1)%N][c] = i
        r, c = nr, nc

    for row in A:
        print(*row)


if __name__ == "__main__":
    main()
