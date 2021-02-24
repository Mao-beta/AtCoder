import sys
import math
from collections import defaultdict
from collections import deque
from functools import lru_cache
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    cum = [0] + list(accumulate(A))

    memo = [[0]*(N+1) for _ in range(N+1)]

    for gap in range(1, N+1):
        for l in range(0, N - gap + 1):
            r = l + gap
            if gap == 1:
                memo[l][r] = A[l]
                continue
            res = cum[r] - cum[l]
            cost = 10**20
            for b in range(l+1, r):
                cost = min(cost, memo[l][b] + memo[b][r])
            memo[l][r] = res + cost

    print(memo[0][N] - cum[N])


if __name__ == "__main__":
    main()
