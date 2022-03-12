import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    N, M = NMI()
    ABC = [NLI() for _ in range(M)]
    INF = float("inf")
    D = [[INF]*N for _ in range(N)]

    for a, b, c in ABC:
        a, b = a-1, b-1
        D[a][b] = c
        D[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    answer = 0
    for a, b, c in ABC:
        a, b = a - 1, b - 1
        unused = 0
        for i in range(N):
            if D[a][i] + D[i][b] <= c:
                unused = 1
        answer += unused
    print(answer)


if __name__ == "__main__":
    main()
