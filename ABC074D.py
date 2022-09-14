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
    A = [NLI() for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if A[i][j] > A[i][k] + A[k][j]:
                    print(-1)
                    exit()

    E = []
    for i in range(N):
        for j in range(i+1, N):
            E.append([A[i][j], i, j])

    E.sort()

    ans = 0
    for a, i, j in E:
        use = True
        for k in range(N):
            if k == i or k == j:
                continue
            if a >= A[i][k] + A[k][j]:
                use = False
        if use:
            ans += a

    print(ans)


if __name__ == "__main__":
    main()
