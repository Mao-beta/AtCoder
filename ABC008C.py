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
    N = NI()
    C = [NI() for _ in range(N)]

    # div[i][j]: ciをcjでわりきれるか
    div = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ci, cj = C[i], C[j]
            if ci % cj == 0:
                div[i][j] = 1

    S = [sum(D) for D in div]

    ans = 0

    for i in range(N):
        s = S[i]
        ans += 0.5 if s % 2 == 0 else (s+1)/2 / s

    print(ans)


if __name__ == "__main__":
    main()
